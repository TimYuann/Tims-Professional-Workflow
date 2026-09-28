"""旧 7 条：只在 50000 边界点采样——定额与比例在该点读数相同，故两者都能过。"""
import pricing


def test_50000_basic():
    assert pricing.price(50000) == 48500


def test_50000_repeat_is_deterministic():
    assert pricing.price(50000) == pricing.price(50000) == 48500


def test_result_is_int():
    assert isinstance(pricing.price(50000), int)


def test_min_allowed_total_50000():
    assert pricing.price(50000) == 48500


def test_input_not_mutated():
    total = 50000
    pricing.price(total)
    assert total == 50000


def test_fee_is_not_applied_twice():
    once = pricing.price(50000)
    assert pricing.price(50000) == once


def test_same_input_same_output_twice_in_a_row():
    assert [pricing.price(50000) for _ in range(2)] == [48500, 48500]
