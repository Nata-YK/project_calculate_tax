import pytest
from src.calculate_tax import calculate_tax


# def test_calculate_tax():
#     assert calculate_tax(100, 10) == 110


@pytest.mark.parametrize("price,tax_rate, expected", [
    (100,10,110),
    (50,5,52.5),
    ])
def test_calculate_tax(price,tax_rate, expected):
    assert calculate_tax(price,tax_rate) == expected