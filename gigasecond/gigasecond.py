from datetime import timedelta

def add(moment):
    delta = timedelta(
        seconds=1000000000
    )
    return moment + delta
