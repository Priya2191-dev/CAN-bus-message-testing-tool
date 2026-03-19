import cantools

def decode_message():
    db = cantools.database.load_file("example.dbc")
    msg = db.get_message_by_name("SpeedMsg")
    return msg.decode(bytes([100,0,0,0,0,0,0,0]))
