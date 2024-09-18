from datetime import datetime
from typing import Any


def date_format(date: Any):
    if isinstance(date, str):
        try:
            moving_date = datetime.strptime(date, "%Y-%m-%d").date()
            return moving_date
        except ValueError as e:
            raise e
    return date
