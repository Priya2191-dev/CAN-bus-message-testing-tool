import can
import logging
import time

logging.basicConfig(level=logging.INFO)

CHANNEL = "test"
BUSTYPE = "virtual"

def get_bus():
    """Create and return a virtual CAN bus"""
    return can.interface.Bus(interface='virtual', channel='test')

def create_message(arbitration_id=0x123, data=None):
    """Create a CAN message"""
    if data is None:
        data = [1, 2, 3, 4]

    return can.Message(
        arbitration_id=arbitration_id,
        data=data,
        is_extended_id=False
    )

def send_message(bus, msg):
    """Send a CAN message safely"""
    try:
        bus.send(msg)
        logging.info(f"Message sent: ID={hex(msg.arbitration_id)}, DATA={list(msg.data)}")
        return True
    except can.CanError as e:
        logging.error(f"Send failed: {e}")
        return False

def receive_message(bus, timeout=2):
    start = time.time()
    while time.time() - start < timeout:
        msg = bus.recv(timeout=0.2)
        if msg:
            return msg
    return None
