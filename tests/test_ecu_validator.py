import pytest
from ecu_validator import validate_speed

def test_valid_speed():
    assert validate_speed(60) == True

def test_invalid_speed():
    with pytest.raises(ValueError):
        validate_speed(200)
