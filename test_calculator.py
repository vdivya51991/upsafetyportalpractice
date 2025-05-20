import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2,3) == 5
def test_subtract():
    assert subtract(4,1) == 3
def test_multiply():
    assert multiply(3,5) == 15
def test_divide():
    assert divide(6,3) == 2
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(6,0)