
"""Late-fee calculation for the campus library desk."""

from typing import Optional


def late_fee(
    days_late: int,
    daily_rate: float,
    grace_days: int = 0,
    max_fee: Optional[float] = None,
) -> float:
    """Calculate the late fee after applying grace days and a maximum fee.

 Items returned on time or within the grace period are not charged.
    Only days beyond the grace period are charged. If max_fee is provided,
    the final fee cannot exceed that amount.
    """
    if days_late <= grace_days:
        return 0.0

    chargeable_days = days_late - grace_days
    fee = round(chargeable_days * daily_rate, 2)

    if max_fee is not None:
        fee = min(fee, max_fee)

    return fee
