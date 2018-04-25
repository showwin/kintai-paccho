from slackbot.bot import listen_to, respond_to

from .components.configuration import configure_employee
from .components.extra import be_shy
from .components.holiday import (
    apply_holiday,
    get_remained_holiday_count,
    help_holiday
)
from .components.time_recorder import record_punch_in, record_punch_out
from .decorator import not_allowed_in_busy_time, write_log


# タイムスタンプの勤怠系
@listen_to('^おはー$')
@respond_to('^おはー$')
@write_log
def record_punch_in_listener(message):
    record_punch_in(message)


@listen_to(r'^(店じまい|おつー)$')
@respond_to(r'^(店じまい|おつー)$')
@write_log
def record_punch_out_listener(message):
    record_punch_out(message)


# 有給系
@respond_to(r'^(?!.*(に有給取得したいです|残休暇日数)).*(?=有給|休暇).+$')
def help_holiday_listener(message, _):
    help_holiday(message)


@respond_to('^残休暇日数$')
@not_allowed_in_busy_time
def get_remained_holiday_count_listener(message):
    get_remained_holiday_count(message)


@respond_to(r'^\d+年\d+月\d+日に有給取得したいです$')
@not_allowed_in_busy_time
def apply_holiday_listener(message):
    apply_holiday(message)


# 設定系
@respond_to('従業員コード')
@not_allowed_in_busy_time
@write_log
def configure_employee_listener(message):
    configure_employee(message)


# おまけ
@respond_to(r'感謝|ありがとう|好き|すごい')
@write_log
def be_shy_listener(message):
    be_shy(message)
