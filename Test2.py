
import os

def calculate_invoice_total(subtotal: float, tax_rate: float) -> float:
    """Calculates final invoice amount with tax."""
    return round(subtotal * (1.0 + tax_rate), 2)

def is_valid_discount(discount_code: str) -> bool:
    """Validates coupon format."""
    return discount_code.startswith("SAVE_")


