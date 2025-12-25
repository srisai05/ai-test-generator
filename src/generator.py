"""
Core Test Case Generation Logic
Fast, Stable & Evaluation-Safe Version
"""

import logging
from src.ollama_client import generate_ai_response

logger = logging.getLogger(__name__)


# =========================================================
# FAST MODE PROMPT  (Default – Runs under 1 minute)
# =========================================================
FAST_PROMPT_TEMPLATE = """
Requirement:
{requirement}

IMPORTANT EXECUTION RULES:
- You are NOT a chatbot
- DO NOT greet
- DO NOT explain anything
- DO NOT use markdown formatting
- ONLY plain text output
- STRICT structure only
- NO emojis
- NO extra narrative sentences
- NO headings other than given

====================================================
TRACEABILITY MATRIX
====================================================
Requirement ID | Scenario Name | Test Case ID | Coverage Status

====================================================
TEST CASES
====================================================

SCENARIO CATEGORY: (Functional / Negative / Boundary / Edge)
SCENARIO NAME:
OBJECTIVE:
TEST CASE ID:
PRIORITY:
SEVERITY:
PRE CONDITIONS:
POST CONDITIONS:

TEST STEPS WITH EXPECTED RESULTS:
1) Step
   Expected Result:
2) Step
   Expected Result:
3) Step
   Expected Result:

EXPECTED FINAL OUTCOME:

------------------------------------

GENERATE EXACTLY:
2 Functional Scenarios
2 Negative Scenarios
1 Boundary Scenario
1 Edge Case Scenario

====================================================
ACCEPTANCE CRITERIA
====================================================
1)
2)
3)

====================================================
TEST SUMMARY
====================================================
Total Scenarios:
Total Test Cases:
Coverage Level (High/Medium/Low):
Risk Level:
Confidence Level:
"""

# =========================================================
# CORE FUNCTION
# =========================================================
def generate_test_cases(requirement: str, mode: str = "fast") -> str:
    """
    Generates structured test cases.
    Fast mode by default (stable for demo).
    mode = "enterprise" will use heavy testing suite
    """

    logger.info("Preparing test case generation request | Mode: %s", mode)

    if mode == "enterprise":
        prompt = ENTERPRISE_PROMPT_TEMPLATE.format(requirement=requirement)
    else:
        prompt = FAST_PROMPT_TEMPLATE.format(requirement=requirement)

    try:
        response = generate_ai_response(prompt)

        if not response or len(response.strip()) == 0:
            logger.error("Empty AI response received")
            raise RuntimeError("No response received from AI")

        # ---- Minimal Structure Validation ----
        key_words = ["SCENARIO", "TEST CASE", "EXPECTED", "RESULT"]

        missing = [k for k in key_words if k.lower() not in response.lower()]
        if missing:
            logger.warning("Output missing expected structure parts: %s", missing)

        logger.info("Test case generation completed successfully")
        return response

    except Exception as e:
        logger.exception("Test case generation failed")
        raise RuntimeError("Test case generation failed") from e
