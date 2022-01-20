import datetime
import json
from enum import IntEnum

from .repo import Employee
from .requester import KOTRequester


def register_user(user, kot_user_code) -> dict:
    requester = KOTRequester()
    resp_dict = requester.get('/employees/{}'.format(kot_user_code))
    employee_key = resp_dict['key']
    Employee.create(user, employee_key)
    return {
        'last_name': resp_dict['lastName'],
        'first_name': resp_dict['firstName']
    }

def update_user_timezone(user, timezone):
    return Employee.update_timezone(user, timezone)

class RecordType(IntEnum):
    CLOCK_IN = 1
    CLOCK_OUT = 2
    START_BREAK = 3
    END_BREAK = 4

def record_time(record_type: RecordType, employee_key):
    requester = KOTRequester()
    payload = json.dumps({
        'time': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00'),
        'date': _get_working_date(),
        'code': record_type.value,
    })
    requester.post('/daily-workings/timerecord/{}'.format(employee_key), payload)

def _get_working_date():
    """
    return today formatting '%Y-%m-%d'.
    before 5:00 AM, return yesterday.
    """
    today = datetime.datetime.now()
    if today.hour < 5:
        return (today - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    return today.strftime('%Y-%m-%d')
