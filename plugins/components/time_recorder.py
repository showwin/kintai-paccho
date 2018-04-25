import datetime
import json

from ..requester import KOTException, KOTRequester
from .helper import get_employee_key


def record_punch_in(message):
    if _timerecord(message, '出勤'):
        message.send(':den_paccho1: < おはー　だこくしたよ〜')


def record_punch_out(message):
    if _timerecord(message, '退勤'):
        message.send(':gas_paccho_1: < おつー　打刻したよー')


def _timerecord(message, record_type):
    if record_type == '出勤':
        code = 1
    elif record_type == '退勤':
        code = 2
    else:
        return False

    employee_key = get_employee_key(message)
    if not employee_key:
        return False

    requester = KOTRequester()
    payload = json.dumps({
        'time': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00'),
        'date': datetime.datetime.now().strftime('%Y-%m-%d'),
        'code': code,
    })
    try:
        requester.post('/daily-workings/timerecord/{}'.format(employee_key), payload)
    except KOTException as e:
        message.send('King of Time でエラーレスポンスが返ってきたぱっちょ！')
        message.send(e)
        return False
    return True
