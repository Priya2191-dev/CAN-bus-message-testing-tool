from fault_injection import inject_fault

def test_fault_injection():
    data = [10, 20, 30]
    faulty = inject_fault(data.copy())
    
    assert faulty[0] == 255
    assert faulty[1:] == [20, 30]
