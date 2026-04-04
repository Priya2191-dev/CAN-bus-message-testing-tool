import logging

logging.basicConfig(level=logging.INFO)


def checksum(data):
    if not isinstance(data, list):
        raise TypeError("Data must be a list")

    if not all(isinstance(x, int) for x in data):
        raise TypeError("All elements must be integers")

    return sum(data) % 256

def verify(data, expected_checksum):
    """
    Verify data integrity using checksum
    """
    
    if not isinstance(expected_checksum, int):
        raise TypeError("Expected checksum must be an integer")

    calculated = checksum(data)

    logging.info(f"Calculated: {calculated}, Expected: {expected_checksum}")

    return calculated == expected_checksum
