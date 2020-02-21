from calculator_simple.calculator import Calculator

calculator = Calculator()

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(1,2,3,4,5,) == 15

def test_multiply():
    assert calculator.multiply(2,7) == 14
    assert calculator.multiply(1,3,1) == 3

    
    

