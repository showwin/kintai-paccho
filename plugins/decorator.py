import functools
import time


def not_allowed_in_busy_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_now_str = time.strftime('%H%M')
        if '0830' < time_now_str < '1000' or '1730' < time_now_str < '1800':
            say_not_allow(*args, **kwargs)
        else:
            func(*args, **kwargs)
    return wrapper


def say_not_allow(message):
    message.send('[08:30 ～ 10:00, 17:30 ～ 18:30] の時間帯はAPIの都合で勤怠登録しかできないんだ。ごめん:paccho:')
