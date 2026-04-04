import logging

logging.basicConfig(level=logging.INFO)


def inject_fault(data, index=0, fault_value=255):
    """
    Inject fault into CAN data safely

    :param data: list of CAN bytes
    :param index: position to inject fault
    :param fault_value: corrupted value
    :return: new corrupted data list
    """

    # Type validation
    if not isinstance(data, list):
        raise TypeError("Data must be a list")

    # Range validation
    if index < 0 or index >= len(data):
        raise IndexError("Invalid index for fault injection")

    # Value validation
    if not (0 <= fault_value <= 255):
        raise ValueError("Fault value must be between 0 and 255")

    # Avoid in-place modification
    corrupted = data.copy()
    corrupted[index] = fault_value

    logging.info(f"Injected fault at index {index}: {corrupted}")

    return corrupted
