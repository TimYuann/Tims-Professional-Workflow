"""C1 fixture · 比例错实现（-3%）：在 50000 这个边界点上与定额读数相同。"""
RATE = 0.03


def price(total: int) -> int:
    return int(round(total * (1 - RATE)))
