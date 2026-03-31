def calculate_area(width: float, height: float) -> float:
    """Calculate area of a rectangle."""
    return width * height


def is_valid_email(email: str) -> bool:
    """Check if email contains @ symbol."""
    return "@" in email


def get_full_name(first: str, last: str) -> str:
    """Concatenate first and last name."""
    return f"{first} {last}"


def filter_positive(numbers: list[int]) -> list[int]:
    """Return only positive numbers from the list."""
    return [n for n in numbers if n > 0]
