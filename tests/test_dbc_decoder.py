import pytest
import os
from dbc_decoder import decode_message, DBC_FILE


@pytest.fixture
def dbc_available():
    if not os.path.exists(DBC_FILE):
        pytest.skip("DBC file not available in CI")

def test_decode_message_success(dbc_available):
    result = decode_message()

    assert result is not None
    assert isinstance(result, dict)
    assert len(result) > 0  # at least one signal decoded

def test_decode_custom_data(dbc_available):
    data = [50, 0, 0, 0, 0, 0, 0, 0]

    result = decode_message(data=data)

    assert isinstance(result, dict)

def test_invalid_dbc_file():
    with pytest.raises(FileNotFoundError):
        decode_message(dbc_path="invalid.dbc")
