from slackbot.bot import listen_to, respond_to

from .components.configuration import configure_employee
from .components.extra import be_shy, i_am_not_alexa, i_am_not_siri
from .components.holiday import (
    apply_holiday,
    get_remained_holiday_count,
    help_holiday
)
from .components.time_recorder import (
    help_rest,
    record_ending_rest,
    record_punch_in,
    record_punch_out,
    record_starting_rest
)
from .decorator import not_allowed_in_busy_time, write_log


# タイムスタンプの勤怠系
@listen_to('^\s*おはー$')
@respond_to('^\s*おはー$')
@write_log
def record_punch_in_listener(message):
    record_punch_in(message)


@listen_to(r'^\s*(店じまい|おつー)$')
@respond_to(r'^\s*(店じまい|おつー)$')
@write_log
def record_punch_out_listener(message, _):
    record_punch_out(message)


@respond_to(r'^\s*(?!.*(休憩開始|休憩終了)).*(?=休憩|一時退社|もぐもぐタイム|抜け).+$')
def help_rest_listener(message, _):
    help_rest(message)


@respond_to('^\s*休憩開始$')
def record_starting_rest_listener(message):
    record_starting_rest(message)


@respond_to('^\s*休憩終了$')
def record_ending_rest_listener(message):
    record_ending_rest(message)


# 有給系
@respond_to(r'^\s*(?!.*(に有給取得したいです|残休暇日数)).*(?=有給|休暇).+$')
def help_holiday_listener(message, _):
    help_holiday(message)


@respond_to('^\s*残休暇日数$')
@not_allowed_in_busy_time
def get_remained_holiday_count_listener(message):
    get_remained_holiday_count(message)


@respond_to(r'^\s*\d+年\d+月\d+日に有給取得したいです$')
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


@respond_to(r'^(アレクサ|Alexa|alexa)$')
@write_log
def i_am_not_alexa_listener(message):
    i_am_not_alexa(message)


@respond_to('^Hey Siri$')
def i_am_not_siri_listener(message):
    i_am_not_siri(message)
