import can

def send_message():
    bus = can.interface.Bus(bustype='virtual')
    msg = can.Message(arbitration_id=0x123, data=[1,2,3,4])
    bus.send(msg)
    return msg
