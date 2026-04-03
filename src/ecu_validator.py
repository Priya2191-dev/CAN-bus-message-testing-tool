import logging

logging.basicConfig(level=logging.INFO)

MIN_SPEED = 0
MAX_SPEED = 120

def validate_speed(speed):
    """
    Validate ECU speed value
    :param speed: numeric speed value
    :return: True if valid
    :raises: TypeError, ValueError
    """
    
    # Type validation
    if not isinstance(speed, (int, float)):
        raise TypeError("Speed must be numeric")

    # Range validation
    if not (MIN_SPEED <= speed <= MAX_SPEED):
        raise ValueError(f"Speed must be between {MIN_SPEED} and {MAX_SPEED}")

    logging.info(f"Valid speed: {speed}")
    return True
