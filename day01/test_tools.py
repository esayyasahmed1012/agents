
from decimal import Decimal

import pytest

from tools import (
    calculate_subtotal,
    calculate_vat,
    calculate_total,
)


def test_calculate_subtotal():
    result = calculate_subtotal(
        Decimal("800"),
        15
    )

    assert result == Decimal("12000")


def test_calculate_vat():
    result = calculate_vat(
        Decimal("12000"),
        Decimal("15")
    )

    assert result == Decimal("1800")


def test_calculate_total():
    result = calculate_total(
        Decimal("12000"),
        Decimal("1800")
    )

    assert result == Decimal("13800")


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_subtotal(
            Decimal("-800"),
            15
        )


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_subtotal(
            Decimal("800"),
            -15
        )


def test_negative_vat():
    with pytest.raises(ValueError):
        calculate_vat(
            Decimal("12000"),
            Decimal("-15")
        )
