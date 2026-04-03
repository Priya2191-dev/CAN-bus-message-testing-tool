import pytest
from ecu_validator import validate_speed


def test_valid_speed():
    assert validate_speed(60) is True

@pytest.mark.parametrize("speed", [0, 50, 120])
def test_boundary_values(speed):
    assert validate_speed(speed) is True

@pytest.mark.parametrize("speed", [-1, 121, 200])
def test_invalid_speed_range(speed):
    with pytest.raises(ValueError):
        validate_speed(speed)

@pytest.mark.parametrize("speed", ["fast", None, []])
def test_invalid_speed_type(speed):
    with pytest.raises(TypeError):
        validate_speed(speed)
