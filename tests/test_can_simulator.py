import pytest
import can
from can_simulator import get_bus, create_message, send_message, receive_message

@pytest.fixture
def bus():
    """Setup and teardown CAN bus"""
    bus = get_bus()
    yield bus
    bus.shutdown()

def test_send_and_receive_message(bus):
    msg = create_message()

    assert send_message(bus, msg) is True

    received = receive_message(bus, timeout=2)

    assert received is not None, "No message received"
    assert received.arbitration_id == msg.arbitration_id
    assert list(received.data) == list(msg.data)

def test_message_data_integrity(bus):
    msg = create_message(data=[10, 20, 30, 40])

    send_message(bus, msg)
    received = receive_message(bus)

    assert list(received.data) == [10, 20, 30, 40]

def test_no_message_timeout(bus):
    received = receive_message(bus, timeout=1)
    assert received is None
