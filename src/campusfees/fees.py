
def late_fee(days_late: int, daily_rate: float, grace_days: int = 0) -> float:
    """Return the late fee after allowing grace_days free days.

    Items returned on time or within the grace period are not charged.
    """
    if days_late <= grace_days:
        return 0.0
    chargeable_days = days_late - grace_days
    return round(chargeable_days * daily_rate, 2)
