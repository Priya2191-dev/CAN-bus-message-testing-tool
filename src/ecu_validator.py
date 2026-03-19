def validate_speed(speed):
    if not (0 <= speed <= 120):
        raise ValueError("Invalid speed")
    return True
