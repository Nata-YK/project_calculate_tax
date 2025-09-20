import pytest

from src.task_2 import calculate_taxes


@pytest.mark.parametrize("price, tax_rate, expected", [
    ([15.6, 31.6], 3.7, [16.1772, 32.769200000000005]),
    ([42.4, 33.1], 5.5, [44.732, 34.920500000000004]),
    ([100.4, 200,7], 3.0, [103.412, 206.0, 7.21]),
    ([54.0, 51.4], 0, [54.0, 51.4]),
])
def test_calculate_taxes(price, tax_rate, expected):
    assert calculate_taxes(price, tax_rate) == expected


def test_calculate_taxes_raises():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
        calculate_taxes([54.0, 51.4], -1)


def test_calculate_taxes_nin_pasitive():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_taxes([54.0, 0], 1.5)