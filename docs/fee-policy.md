
# Late Fee Policy

The campus library desk charges late fees according to these rules:

- Fees accrue per calendar day an item is late, at the item's daily rate.
- Items returned on time or early are never charged.
- **Grace period:** The first `grace_days` days late are free. Fees are charged only for days beyond the grace period.
- **Maximum fee:** When `max_fee` is specified, the total late fee cannot exceed that amount.
- **Calculation order:** The grace period is applied first, followed by the maximum fee cap.
