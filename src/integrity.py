import logging

logging.basicConfig(level=logging.INFO)

def checksum(data):
    """
    Calculate checksum (1-byte)
    :param data: list of integers
    :return: checksum value (0-255)
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list")

    if not all(isinstance(x, int) for x in data):
        raise TypeError("All elements must be integers")

    return sum(data) % 256

def verify(data, expected_checksum):
    """
    Verify data integrity using checksum
    :param data: list of integers
    :param expected_checksum: checksum to validate against
    :return: True if valid, False otherwise
    """
    calculated = checksum(data)

    logging.info(f"Calculated: {calculated}, Expected: {expected_checksum}")

    return calculated == expected_checksum
