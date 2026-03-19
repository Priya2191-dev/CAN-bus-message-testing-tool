import can
from can_simulator import send_message

def test_send_message():
    msg = send_message()
    assert msg.arbitration_id == 0x123
    assert list(msg.data) == [1, 2, 3, 4]
