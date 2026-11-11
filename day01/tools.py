
from decimal import Decimal


def calculate_subtotal(
    price: Decimal,
    quantity: int
) -> Decimal:

    if price < 0:
        raise ValueError("Price cannot be negative.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    return price * quantity


def calculate_vat(
    amount: Decimal,
    vat_rate: Decimal
) -> Decimal:

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if vat_rate < 0:
        raise ValueError("VAT rate cannot be negative.")

    return amount * vat_rate / Decimal("100")


def calculate_total(
    subtotal: Decimal,
    vat: Decimal
) -> Decimal:

    if subtotal < 0 or vat < 0:
        raise ValueError("Amounts cannot be negative.")

    return subtotal + vat
