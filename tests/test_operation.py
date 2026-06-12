from src.math_operation import add, substract

def test_add():
    assert add(2, 3) == 5 # assert means that the expected value is 5 and the actual value is also 5, if not then it will raise an error 
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_substract():
    assert substract(5, 2) == 3
    assert substract(0, 1) == -1
    assert substract(10, 5) == 5

