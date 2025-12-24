import os
import pytest
from src.generator import generate_test_cases

def test_ollama_failure_handling():
    os.environ["SIMULATE_FAIL"] = "1"

    with pytest.raises(RuntimeError):
        generate_test_cases("Login System")

    del os.environ["SIMULATE_FAIL"]
