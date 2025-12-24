import os
import pytest
from src.generator import generate_test_cases

def test_ollama_failure():
    os.environ["SIMULATE_FAIL"] = "1"
    with pytest.raises(RuntimeError):
        generate_test_cases("Login system")

    del os.environ["SIMULATE_FAIL"]
