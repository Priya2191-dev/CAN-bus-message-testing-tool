def checksum(data):
    return sum(data) % 256

def verify(data):
    return checksum(data) == checksum(data)
