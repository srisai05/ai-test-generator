from src.generator import generate_test_cases
import pytest

def test_ai_response_structure():
    requirement = "User must login using username and password"
    response = generate_test_cases(requirement)

    assert "Functional" in response
    assert "Negative" in response
    assert "Boundary" in response

