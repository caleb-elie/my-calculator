from datetime import datetime
from functools import wraps


def watch_clock(func):
    @wraps(func)
    def calculateTime(*args, **kwargs):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time:", current_time)
        return func(*args, **kwargs)

    return calculateTime


@watch_clock
def sayTime():
    print("Executing say_time function")


sayTime()
