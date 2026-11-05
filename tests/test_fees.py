
from campusfees import late_fee


def test_on_time_return_is_free():
    assert late_fee(0, 0.25) == 0.0


def test_early_return_is_free():
    assert late_fee(-2, 0.25) == 0.0


def test_one_day_late():
    assert late_fee(1, 0.25) == 0.25


def test_multiple_days_late():
    assert late_fee(4, 0.25) == 1.0


def test_fee_rounds_to_cents():
    assert late_fee(3, 0.333) == 1.0


# Verify that items returned within the grace period have no late fee.
def test_within_grace_period():
    assert late_fee(2, 0.25, grace_days=3) == 0.0


# Verify that fees apply only to days beyond the grace period.
def test_past_grace_period():
    assert late_fee(5, 0.25, grace_days=3) == 0.50


# Verify that the late fee cannot exceed the maximum fee.
def test_fee_is_capped_at_max_fee():
    assert late_fee(40, 0.25, max_fee=5.0) == 5.0


# Verify that fees below the maximum remain unchanged.
def test_fee_below_cap_is_unchanged():
    assert late_fee(4, 0.25, max_fee=5.0) == 1.0


# Verify that the grace period is applied before the maximum fee.
def test_grace_period_and_fee_cap_together():
    assert late_fee(10, 1.0, grace_days=3, max_fee=5.0) == 5.0
    assert late_fee(5, 1.0, grace_days=3, max_fee=5.0) == 2.0
