from log_replay import replay

def test_log_replay(capsys):
    log = [{"id": 0x101, "data": [1, 2]}]
    
    replay(log)
    
    captured = capsys.readouterr()
    assert "Replay" in captured.out
