def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total cost based on price and quantity.

    Args:
        price (float): The price of a single item.
        quantity (int): The number of items.

    Returns:
        float: The total cost.
    """
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative.")    
    return price * quantity

if __name__ == "__main__":
    # Example usage
    price = 10.0
    quantity = 5
    total_cost = calculate_total(price, quantity)
    print(f"Total cost for {quantity} items at ${price} each is: ${total_cost}")
