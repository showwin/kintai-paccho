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


def record_starting_rest(message):
    if _timerecord(message, '休憩開始'):
        message.send(':gas_paccho_1: < はーい　ゆっくり休んでねー')


def record_ending_rest(message):
    if _timerecord(message, '休憩終了'):
        message.send(':den_paccho1: < おっけー　がんばっていこ〜')


def help_rest(message):
    message.send('休憩するときは "@kintai-paccho 休憩開始" っていうぱっちょ')
    message.send('再開するときは "@kintai-paccho 休憩終了" だぱっちょ')


def _timerecord(message, record_type):
    record_map = {
        '出勤': 1,
        '退勤': 2,
        '休憩開始': 3,
        '休憩終了': 4,
    }
    employee_key = get_employee_key(message)
    if not employee_key:
        return False

    requester = KOTRequester()
    payload = json.dumps({
        'time': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00'),
        'date': datetime.datetime.now().strftime('%Y-%m-%d'),
        'code': record_map[record_type],
    })
    try:
        requester.post('/daily-workings/timerecord/{}'.format(employee_key), payload)
    except KOTException as e:
        message.send('King of Time でエラーレスポンスが返ってきたぱっちょ！')
        message.send(e)
        return False
    return True
