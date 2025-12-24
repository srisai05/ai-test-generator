"""
Core test case generation logic
"""

from ollama_client import generate_ai_response
import logging

logger = logging.getLogger(__name__)

PROMPT_TEMPLATE = """
You are a senior QA Architect.
Generate COMPLETE professional test cases.

Requirement:
{requirement}

Output MUST include:
Strict Output Format:
------------------------------------
Functional Test Cases:
1.
2.

Boundary Test Cases:
1.
2.

Negative Test Cases:
1.
2.

Edge Cases:
1.
2.

Acceptance Criteria:
1.
2.
------------------------------------
NO EXTRA TEXT
ONLY THIS FORMAT
"""

def generate_test_cases(requirement: str):
    logger.info("Preparing test case generation request")
    prompt = PROMPT_TEMPLATE.format(requirement=requirement)
    response = generate_ai_response(prompt)
    logger.info("Test case generation completed")
    return response
