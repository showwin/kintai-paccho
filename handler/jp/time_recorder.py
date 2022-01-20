from components.repo import Employee
from components.requester import KOTException
from components.typing import SlackRequest
from components.usecase import RecordType, record_time

from .helper import response_configuration_help, response_kot_error


def record_clock_in(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)
    timezone = Employee.get_timezone(request.user_id)

    try:
        record_time(RecordType.CLOCK_IN, employee_key, timezone)
        say(':den_paccho1: < おはー　だこくしたよ〜')
    except KOTException as e:
        response_kot_error(say, e)


def record_clock_out(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)
    timezone = Employee.get_timezone(request.user_id)

    try:
        record_time(RecordType.CLOCK_OUT, employee_key, timezone)
        say(':gas_paccho_1: < おつー　打刻したよー')
    except KOTException as e:
        response_kot_error(say, e)


def record_start_break(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)
    timezone = Employee.get_timezone(request.user_id)

    try:
        record_time(RecordType.START_BREAK, employee_key, timezone)
        say(':gas_paccho_1: < はーい　ゆっくり休んでねー')
    except KOTException as e:
        response_kot_error(say, e)



def record_end_break(say, request: SlackRequest):
    employee_key = Employee.get_key(request.user_id)
    if not employee_key:
        return response_configuration_help(say)
    timezone = Employee.get_timezone(request.user_id)

    try:
        record_time(RecordType.END_BREAK, employee_key, timezone)
        say(':den_paccho1: < おっけー　がんばっていこ〜')
    except KOTException as e:
        response_kot_error(say, e)
