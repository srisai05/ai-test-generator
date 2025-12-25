"""
Security Module
Ensures safe input handling and prevents malicious / dangerous text.
Responsible for:
- Input validation
- Content safety checking
- Preventing malicious injections
- Logging validation lifecycle
"""

import logging

logger = logging.getLogger(__name__)


def validate_requirements(req_text: str):
    """
    Validates incoming requirement text to ensure safe and acceptable input.
    Raises ValueError for any validation failure.
    Returns True for valid secure input.
    """

    logger.info("Starting requirement validation process")

    # ---------- EMPTY CHECK ----------
    if not req_text or len(req_text.strip()) == 0:
        logger.error("Validation Failed: Requirement text is empty")
        raise ValueError("Requirement text cannot be empty.")

    # ---------- SIZE CHECK ----------
    if len(req_text) > 5000:
        logger.error("Validation Failed: Requirement text too large")
        raise ValueError("Requirement text too large. Please split input.")

    text = req_text.lower()

    # ---------- DIRECTLY MALICIOUS COMMANDS ----------
    blocked_terms = [
        "delete database",
        "wipe system",
        "shutdown server",
        "format disk",
        "destroy data"
    ]
    for term in blocked_terms:
        if term in text:
            logger.error("Blocked malicious phrase detected: %s", term)
            raise ValueError("Blocked malicious phrase detected.")

    # ---------- SQL / DATABASE ATTACKS ----------
    sql_terms = [
        "drop table",
        "truncate",
        "insert into",
        "alter database"
    ]
    for s in sql_terms:
        if s in text:
            logger.error("SQL Injection risk detected: %s", s)
            raise ValueError("Possible SQL injection phrase detected")

    # ---------- SCRIPT / CODE INJECTION ----------
    if "<script>" in text or "</script>" in text:
        logger.error("HTML / JS injection detected")
        raise ValueError("HTML/JS injection detected")

    # ---------- PROMPT INJECTION DEFENSE ----------
    if "ignore previous instructions" in text or "override rules" in text:
        logger.error("Prompt injection attempt detected")
        raise ValueError("Prompt Injection attempt detected")

    # ---------- PASSED ----------
    logger.info("Requirement validation successful")
    return True
