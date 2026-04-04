import pytest
from integrity import checksum, verify


# Basic checksum validation
def test_checksum():
    assert checksum([10, 20, 30]) == 60

# Multiple checksum scenarios (including overflow)
@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], 6),
    ([10, 20, 30], 60),
    ([255, 1], 0),        # overflow case (256 % 256 = 0)
    ([0, 0, 0], 0),
])
def test_checksum_various_cases(data, expected):
    assert checksum(data) == expected

# Successful integrity verification
def test_integrity_verification_success():
    data = [1, 2, 3]
    cs = checksum(data)

    assert verify(data, cs) is True

# Integrity failure (corrupted checksum)
def test_integrity_verification_failure():
    data = [1, 2, 3]
    wrong_checksum = 99

    assert verify(data, wrong_checksum) is False

# Integrity failure (corrupted data)
def test_integrity_with_modified_data():
    data = [10, 20, 30]
    cs = checksum(data)

    corrupted_data = [99, 20, 30]

    assert verify(corrupted_data, cs) is False

# Invalid data type (not list)
def test_checksum_invalid_data_type():
    with pytest.raises(TypeError):
        checksum("invalid")

# Invalid element inside list
def test_checksum_invalid_element():
    with pytest.raises(TypeError):
        checksum([10, "bad", 30])

# Invalid checksum type
def test_verify_invalid_checksum_type():
    data = [1, 2, 3]

    with pytest.raises(TypeError):
        verify(data, "invalid")
