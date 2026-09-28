"""C1 fixture · 定额实现（-1500 元），规则来自 /tmp 现场冻结契约 S4。"""
FEE = 1500


def price(total: int) -> int:
    return total - FEE
