"""
CLI Entry Point
"""

import logging
from logging.handlers import RotatingFileHandler
from src.generator import generate_test_cases
from src.security import validate_requirements


logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("logs/app.log", maxBytes=500000, backupCount=3)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def main():
    print("===== AI TEST CASE GENERATOR USING OLLAMA =====")
    requirement = input("\nEnter Requirement: ")

    try:
        validate_requirements(requirement)
        result = generate_test_cases(requirement)

        print("\n===== GENERATED TEST CASES =====\n")
        print(result)

    except Exception as e:
        logger.exception("Execution failed")
        print("Error:", str(e))

if __name__ == "__main__":
        main()
