from datetime import datetime
from datetime import timedelta

def add_gigasecond(start_date):
    gigasecond = timedelta(seconds=10**9)
    return start_date + gigasecond