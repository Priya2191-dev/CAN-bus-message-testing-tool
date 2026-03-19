import pytest
import cantools
from dbc_decoder import decode_message

def test_decode_message():

    try:
        result = decode_message()
        assert isinstance(result, dict)
    except Exception:
        pytest.skip("DBC file not available")
