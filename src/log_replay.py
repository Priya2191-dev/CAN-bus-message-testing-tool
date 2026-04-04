import logging

logging.basicConfig(level=logging.INFO)

def replay(log):
    """
    Replay CAN log frames

    :param log: list of CAN frames (dict)
    """
    if not isinstance(log, list):
        raise TypeError("Log must be a list")

    for frame in log:
        if not isinstance(frame, dict):
            raise TypeError("Each frame must be a dictionary")

        if "id" not in frame or "data" not in frame:
            raise ValueError("Frame must contain 'id' and 'data'")

        output = f"Replay: ID={hex(frame['id'])}, DATA={frame['data']}"
        print(output)
        logging.info(output)
