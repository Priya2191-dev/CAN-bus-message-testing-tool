import cantools
import os
import logging

logging.basicConfig(level=logging.INFO)

DBC_FILE = "example.dbc"
MESSAGE_NAME = "SpeedMsg"

def load_dbc(dbc_path=DBC_FILE):
    """Load DBC file safely"""
    if not os.path.exists(dbc_path):
        raise FileNotFoundError(f"DBC file not found: {dbc_path}")
    return cantools.database.load_file(dbc_path)

def get_message(db, message_name=MESSAGE_NAME):
    """Fetch message from DBC"""
    msg = db.get_message_by_name(message_name)
    if msg is None:
        raise ValueError(f"Message {message_name} not found in DBC")
    return msg

def decode_message(data=None, dbc_path=DBC_FILE):
    """
    Decode CAN message using DBC
    :param data: list of 8 bytes
    :param dbc_path: path to dbc file
    :return: dict of decoded signals
    """
    if data is None:
        data = [100, 0, 0, 0, 0, 0, 0, 0]

    db = load_dbc(dbc_path)
    msg = get_message(db)

    decoded = msg.decode(bytes(data))
    logging.info(f"Decoded message: {decoded}")

    return decoded
