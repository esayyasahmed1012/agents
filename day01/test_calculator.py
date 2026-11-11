import pytest
from calculator import calculate_total

def test_normal_calculation():
    assert calculate_total(10.0, 5) == 50.0
    assert calculate_total(0.0, 10) == 0.0
    assert calculate_total(15.5, 2) == 31.0

def test_negative_values():
    with pytest.raises(ValueError):
        calculate_total(-10.0, 5)
    with pytest.raises(ValueError):
        calculate_total(10.0, -5)
def test_zero_quantity():
    assert calculate_total(10.0, 0) == 0.0
def test_zero_price():
    assert calculate_total(0.0, 5) == 0.0