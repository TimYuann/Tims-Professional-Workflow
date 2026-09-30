def normalize_label(value: str) -> str:
    """Normalize a label for display."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return value.strip().upper()
