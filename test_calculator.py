from calculator import binary_calculator

def test_addition():
    assert binary_calculator("00000001", "00000001", "+") == "00000010" # All work
    assert binary_calculator("00000010", "00000010", "+") == "00000100"
    assert binary_calculator("00000001", "00000010", "+") == "00000011"

def test_subtraction():
    assert binary_calculator("00000010", "00000001", "-") == "00000001" # All work
    assert binary_calculator("00000010", "00000010", "-") == "00000000"

def test_multiplication():
    assert binary_calculator("00000010", "00000010", "*") == "00000100" # All work
    assert binary_calculator("00000011", "00000010", "*") == "00000110"

def test_division():
    assert binary_calculator("00000100", "00000010", "/") == "00000010"
    assert binary_calculator("00000011", "00000111", "/") == "00000000" 
    assert binary_calculator("00000100", "00000000", "/") == "NaN"

def test_invalid_input():
    assert binary_calculator("00000002", "00000001", "+") == "Error"
    assert binary_calculator("00000001", "00000002", "+") == "Error"
    assert binary_calculator("abcd", "1", "+") == "Error"
    assert binary_calculator("1", "abcd", "+") == "Error"

def test_overflow():
    assert binary_calculator("11111111", "00000001", "+") == "Overflow" # All work
    assert binary_calculator("11111111", "00000011", "*") == "Overflow"
    assert binary_calculator("00000001", "00000011", "-") == "Overflow"
