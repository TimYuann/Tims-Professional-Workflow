"""新判据：旧 7 条 + 一个非边界 witness（51000 → 49500）。
定额实现：51000-1500=49500；比例实现：51000*0.97=49470 → 可区分。"""
import pricing

from test_pricing_old import *  # noqa: F401,F403  (旧 7 条保持)


def test_non_boundary_witness_51000_is_49500():
    assert pricing.price(51000) == 49500
