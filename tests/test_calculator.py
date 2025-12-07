from financial_calc.calculator import *
import pytest


def test_simple_interest():
    assert calculate_simple_interest(100, 10, 2) == 20
    assert calculate_simple_interest(200, 10, 4) == 80
    assert calculate_simple_interest(0, 0, 0) == 0
    with pytest.raises(ValueError):
        calculate_simple_interest(-100, 2, 3)

def test_compound_interest():
    # 100 * 1.21 = 121
    assert calculate_compound_interest(100, 10, 2) == 121.00
    # res = principal * (1 + rate/(100*n))**(n*time)
    # (1 + 10/200)**(2*4) = 1.05**8 = 1.4775
    assert calculate_compound_interest(100, 10, 4, 2) == 147.75
    assert calculate_compound_interest(100, 0, 0) == 100
    with pytest.raises(ValueError):
        calculate_compound_interest(100, -0.3, 2)

def test_calculate_tax():
    assert calculate_tax(100, 32) == 32
    assert calculate_tax(100000, 12) == 12000
    assert calculate_tax(100, 0) == 0
    with pytest.raises(ValueError):
        calculate_tax(100, -10)

    