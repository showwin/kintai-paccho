from components.repo import Employee
from components.requester import KOTException
from components.typing import SlackRequest
from components.usecase import RecordType, record_time

from .helper import response_configuration_help, response_kot_error


def record_clock_in(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)

    try:
        record_time(RecordType.CLOCK_IN, employee_key)
        say(':takopi_2: < おはようだっピ！　打刻したっピ')
    except KOTException as e:
        response_kot_error(say, e)


def record_clock_in_oha(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)

    say(':takopi_1: < おはー　ってなんだっピ…？　タコピー語（？）で言ってほしいっピ！')


def record_clock_in_uzai(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)

    say(':takopi_3: < なんだか元気がなさそうだっピね…　もっと元気に言ってほしいっピ！！')


def record_wakaran(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)

    say(':takopi_5: < な、なんのことだかわかんないっピ…　タコピー語（？）で言ってほしいっピ！')


def record_clock_out(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)

    try:
        record_time(RecordType.CLOCK_OUT, employee_key)
        say(':takopi_2: < おつかれさまだっピ！　打刻したっピ')
    except KOTException as e:
        response_kot_error(say, e)


def record_start_break(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)

    try:
        record_time(RecordType.START_BREAK, employee_key)
        say(':takopi_2: < わかったっピ！　ゆっくり休むっピ')
    except KOTException as e:
        response_kot_error(say, e)


def record_end_break(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)

    try:
        record_time(RecordType.END_BREAK, employee_key)
        say(':takopi_2: < わかったッピ！　がんばるッピ〜')
    except KOTException as e:
        response_kot_error(say, e)
