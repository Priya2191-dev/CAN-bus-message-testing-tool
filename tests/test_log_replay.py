import pytest
from log_replay import replay


def test_log_replay_output(capsys):
    log = [{"id": 0x101, "data": [1, 2]}]

    replay(log)

    captured = capsys.readouterr()
    assert "Replay: ID=0x101" in captured.out

def test_multiple_frames(capsys):
    log = [
        {"id": 0x101, "data": [1, 2]},
        {"id": 0x102, "data": [3, 4]},
    ]

    replay(log)

    captured = capsys.readouterr()
    assert "0x101" in captured.out
    assert "0x102" in captured.out

def test_empty_log(capsys):
    replay([])

    captured = capsys.readouterr()
    assert captured.out == ""

def test_invalid_log_type():
    with pytest.raises(TypeError):
        replay("invalid")

def test_invalid_frame_structure():
    with pytest.raises(ValueError):
        replay([{"id": 0x101}])  # missing data

def test_invalid_frame_type():
    with pytest.raises(TypeError):
        replay([123])
