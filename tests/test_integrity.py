from integrity import checksum, verify

def test_checksum():
    assert checksum([10, 20, 30]) == 60

def test_integrity_verification():
    assert verify([1, 2, 3]) == True
