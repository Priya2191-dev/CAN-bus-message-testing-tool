import pytest
from fault_injection import inject_fault

def test_fault_injection_default():
    data = [10, 20, 30]
    result = inject_fault(data)

    assert result[0] == 255
    assert result[1:] == [20, 30]
    assert data == [10, 20, 30]  # original unchanged

@pytest.mark.parametrize("index", [0, 1, 2])
def test_fault_injection_different_positions(index):
    data = [10, 20, 30]
    result = inject_fault(data, index=index)

    assert result[index] == 255

def test_invalid_index():
    with pytest.raises(IndexError):
        inject_fault([10, 20], index=5)

def test_invalid_data_type():
    with pytest.raises(TypeError):
        inject_fault("invalid")

def test_invalid_fault_value():
    with pytest.raises(ValueError):
        inject_fault([10, 20, 30], fault_value=300)
