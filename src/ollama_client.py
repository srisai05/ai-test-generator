"""
Handles communication with Ollama Gen AI.
Acts as an abstraction layer so the rest of the system
does not depend directly on subprocess execution.

Responsibilities:
- Build AI command
- Execute OLLAMA safely
- Handle failures
- Provide test simulation failure mode
- Log full lifecycle
"""

import subprocess
import yaml
import logging
import os

# ================= CONFIG LOAD =================
with open("config/settings.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

logger = logging.getLogger(__name__)

def generate_ai_response(prompt: str) -> str:
    """
    Sends prompt to Ollama and returns AI response.
    Safe for Windows CP1252 + UTF-8 output.
    Includes:
    - Failure simulation
    - Timeout handling
    - UTF-8 safe decoding
    - Strong logging
    """

    try:
        logger.info("Preparing AI request to Ollama model: %s", CONFIG.get("model"))

        # -------- Failure Simulation Mode --------
        if os.getenv("SIMULATE_FAIL") == "1":
            logger.error("Simulated Ollama Failure Triggered")
            raise RuntimeError("Simulated Ollama Engine Failure")

        # -------- Build Execution Command --------
        cmd = [
            "ollama", "run",
            CONFIG["model"],
          
            prompt
        ]

        logger.info("Sending request to Ollama engine")

        # -------- EXECUTE IN BINARY MODE --------
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=False   # <-- CRITICAL (prevents cp1252 decode)
        )

        stdout, stderr = process.communicate(timeout=300)

        # -------- FORCE UTF-8 SAFE DECODE --------
        stdout = stdout.decode("utf-8", errors="replace") if stdout else ""
        stderr = stderr.decode("utf-8", errors="replace") if stderr else ""

        # -------- Handle Process Failure --------
        if process.returncode != 0:
            logger.error(
                "Ollama execution failed | Return Code: %s | Error: %s",
                process.returncode,
                stderr
            )
            raise RuntimeError("Ollama execution failed")

        if not stdout.strip():
            logger.error("Ollama returned empty response")
            raise RuntimeError("Empty response received from AI")

        logger.info("AI response received successfully")
        return stdout

    except subprocess.TimeoutExpired:
        logger.exception("Ollama process timed out")
        raise RuntimeError("Ollama request timed out")

    except Exception as e:
        logger.exception("AI processing error")
        raise RuntimeError("AI processing error") from e
