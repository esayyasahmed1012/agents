import pytest

from decimal import Decimal

from tool_registry import execute_tool

def test_execute_subtotal():

    result = execute_tool(
        "calculate_subtotal",
        {
            "price": 800,
            "quantity": 15
        }
    )

    assert result == Decimal("12000")


def test_execute_vat():

    result = execute_tool(
        "calculate_vat",
        {
            "amount": 12000,
            "vat_rate": 15
        }
    )

    assert result == Decimal("1800")


def test_execute_total():

    result = execute_tool(
        "calculate_total",
        {
            "subtotal": 12000,
            "vat": 1800
        }
    )

    assert result == Decimal("13800")


def test_unknown_tool():

    with pytest.raises(ValueError):
        execute_tool(
            "delete_database",
            {}
        )


def test_missing_argument():

    with pytest.raises(TypeError):
        execute_tool(
            "calculate_subtotal",
            {"price": 800}
        )
