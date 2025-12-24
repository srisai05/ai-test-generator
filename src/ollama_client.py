"""
Handles communication with Ollama Gen AI
"""

import subprocess
import yaml
import logging
import os

with open("config/settings.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

logger = logging.getLogger(__name__)

def generate_ai_response(prompt: str) -> str:
    try:
        # -------- Improvement: Allow Failure Simulation For Testing --------
        if os.getenv("SIMULATE_FAIL") == "1":
            logger.error("Simulated Ollama Failure Triggered")
            raise RuntimeError("Simulated Ollama Engine Failure")

        # -------- Actual OLLAMA Execution --------
        cmd = [
            "ollama", "run",
            CONFIG["model"],
            prompt
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            logger.error("Ollama execution failed: %s", result.stderr)
            raise RuntimeError("Ollama execution failed")

        logger.info("AI response received successfully")
        return result.stdout

    except Exception as e:
        logger.exception("AI processing error")
        raise RuntimeError("AI processing error") from e
