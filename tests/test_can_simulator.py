import pytest
import can
from can_simulator import get_bus, create_message, send_message, receive_message

@pytest.fixture
def buses():
    """Create TX and RX buses"""
    bus_tx = get_bus()
    bus_rx = get_bus()
    yield bus_tx, bus_rx
    bus_tx.shutdown()
    bus_rx.shutdown()

def test_send_and_receive_message(buses):
    bus_tx, bus_rx = buses

    msg = create_message()

    assert send_message(bus_tx, msg) is True

    received = receive_message(bus_rx, timeout=2)

    assert received is not None, "No message received"
    assert received.arbitration_id == msg.arbitration_id
    assert list(received.data) == list(msg.data)

def test_message_data_integrity(buses):
    bus_tx, bus_rx = buses

    msg = create_message(data=[10, 20, 30, 40])

    send_message(bus_tx, msg)
    received = receive_message(bus_rx, timeout=2)

    assert received is not None, "No message received"
    assert list(received.data) == [10, 20, 30, 40]

def test_no_message_timeout(buses):
    _, bus_rx = buses

    received = receive_message(bus_rx, timeout=1)
    assert received is None
