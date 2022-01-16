import time

def get_now_str() -> str:
    time_str = time.strftime("%Y-%m-%d %H:%M:%S")
    return time_str