from datetime import datetime, timedelta
from typing import List


def calculate_deposit(date: str, periods: int, amount: int, rate: float) -> List[dict]:
    start_date = datetime.strptime(date, "%d.%m.%Y")
    monthly_rate = rate / 100 / 12
    result = {}

    for period in range(1, periods + 1):
        amount += amount * monthly_rate
        result[(start_date + timedelta(days=30*period)).strftime("%d.%m.%Y")] = round(amount, 2)

    return result
