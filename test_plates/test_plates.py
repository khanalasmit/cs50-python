from plates import is_valid

def test_valid_plates():
    assert is_valid("AB1234") == True
    assert is_valid("ABC123") == True
    assert is_valid("AB") == True
    assert is_valid("ABC") == True

def test_invalid_plates():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("A1") == False
    assert is_valid("123456") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB0123") == False
    assert is_valid("A B 1 2") == False
    assert is_valid("AB@123") == False

def test_edge_cases():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("AB1") == True
    assert is_valid("AB123") == True
