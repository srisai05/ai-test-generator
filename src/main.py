"""
CLI Entry Point
"""

import logging
import os
from logging.handlers import RotatingFileHandler

from src.generator import generate_test_cases
from src.security import validate_requirements


# ---------------- LOGGING SETUP ----------------
LOG_PATH = "logs/app.log"

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger()          # root logger
logger.setLevel(logging.INFO)

# Avoid attaching multiple handlers
if not logger.handlers:
    handler = RotatingFileHandler(LOG_PATH, maxBytes=500000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.info("Application Started (CLI Mode)")


# ---------------- MAIN EXECUTION ----------------
def main():
    print("===== AI TEST CASE GENERATOR USING OLLAMA =====")
    requirement = input("\nEnter Requirement: ")

    try:
        logger.info("User entered requirement")
        validate_requirements(requirement)

        logger.info("Requirement validation successful")
        result = generate_test_cases(requirement)

        logger.info("Test case generation completed successfully")

        print("\n===== GENERATED TEST CASES =====\n")
        print(result)

    except Exception as e:
        logger.exception("Execution failed due to error")
        print("Error:", str(e))


if __name__ == "__main__":
    main()
