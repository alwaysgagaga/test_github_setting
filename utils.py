def calculate_total(items):
    """Calculate total price of items."""
    total = 0
    for item in items:
        if item["price"] > 0:
            if item["quantity"] > 0:
                total += item["price"] * item["quantity"]
    return total


def format_name(first, last):
    """Format full name."""
    x = first.strip()
    y = last.strip()
    return x + " " + y
