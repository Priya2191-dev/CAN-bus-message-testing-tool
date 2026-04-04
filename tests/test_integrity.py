import pytest
from integrity import checksum, verify


def test_checksum_basic():
    assert checksum([10, 20, 30]) == 60

@pytest.mark.parametrize("data,expected", [
    ([1, 2, 3], 6),
    ([255, 1], 0),  # overflow case
])
def test_checksum_cases(data, expected):
    assert checksum(data) == expected

def test_verify_success():
    data = [10, 20, 30]
    cs = checksum(data)

    assert verify(data, cs) is True

def test_verify_failure():
    data = [10, 20, 30]
    wrong_cs = 99

    assert verify(data, wrong_cs) is False

def test_invalid_data_type():
    with pytest.raises(TypeError):
        checksum("invalid")

def test_invalid_data_elements():
    with pytest.raises(TypeError):
        checksum([10, "bad", 30])
