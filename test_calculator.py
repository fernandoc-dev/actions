import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 5) == 4

def test_subtract():
    assert calculator.subtract(7, 3) == 4
    assert calculator.subtract(2, 9) == -7

def test_multiply():
    assert calculator.multiply(4, 5) == 20
    assert calculator.multiply(-3, 2) == -6

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(8, 4) == 2

def test_divide_by_zero():
    try:
        calculator.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"