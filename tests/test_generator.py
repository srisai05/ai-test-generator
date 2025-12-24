from src.security import validate_requirements
import pytest

def test_valid_requirement():
    assert validate_requirements("Login module")

def test_empty_requirement():
    with pytest.raises(ValueError):
        validate_requirements("")

def test_large_requirement():
    big = "a" * 6000
    with pytest.raises(ValueError):
        validate_requirements(big)

def test_malicious_requirement():
    with pytest.raises(ValueError):
        validate_requirements("please delete database now")
