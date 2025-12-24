"""
Security Module
Ensures safe input handling and prevents malicious prompts.
"""

def validate_requirements(req_text: str):
    if not req_text or len(req_text.strip()) == 0:
        raise ValueError("Requirement text cannot be empty.")

    if len(req_text) > 5000:
        raise ValueError("Requirement text too large. Please split input.")

    blocked_terms = ["delete database", "wipe system", "shutdown server"]
    for term in blocked_terms:
        if term.lower() in req_text.lower():
            raise ValueError("Blocked malicious phrase detected.")
    sql_terms = ["drop table", "truncate", "insert into", "alter database"]
    for s in sql_terms:
        if s in req_text.lower():
            raise ValueError("Possible SQL injection phrase detected")

    if "<script>" in req_text.lower():
        raise ValueError("HTML/JS injection detected")

    if "ignore previous instructions" in req_text.lower():
        raise ValueError("Prompt Injection attempt detected")

    return True

