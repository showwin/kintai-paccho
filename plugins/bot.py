import datetime
import functools
import json
import time

from slackbot.bot import listen_to, respond_to

from .decorator import not_allowed_in_busy_time
from .employee import Employee
from .logger import write_log
from .requester import KOTException, KOTRequester


# 出勤
@listen_to('^おはー$')
@respond_to('^おはー$')
@write_log
def start_timerecord(message):
    if _timerecord(message, '出勤'):
        message.send(':den_paccho1: < おはー　だこくしたよ〜')


# 退勤
@listen_to(r'^(店じまい|おつー)$')
@respond_to(r'^(店じまい|おつー)$')
@write_log
def end_timerecord(message):
    if _timerecord(message, '退勤'):
        message.send(':gas_paccho_1: < おつー　打刻したよー')


# 初回設定
@respond_to('従業員コード')
@not_allowed_in_busy_time
@write_log
def set_employee_key(message):
    # 従業員コードを抜き出す
    user = _get_user(message)
    try:
        code_str = message.body['text'].split('従業員コード')[1].strip()
        if not code_str:
            raise IndexError
    except IndexError:
        message.send('{user}くん従業員コードが読み取れなかったよ'.format(user=user))
        message.send('"@kintai-paccho 従業員コード 1234" のように入力するぱっちょ！')
        return

    requester = KOTRequester()
    try:
        resp_dict = requester.get('/employees/{}'.format(code_str))
    except KOTException as e:
        message.send('King of Time でエラーレスポンスが返ってきたぱっちょ！')
        message.send(e)
    employee_key = resp_dict['key']
    Employee.create(user, employee_key)
    message.send('{user}さんの設定が完了したぱっちょ！'.format(user=user))


# おまけ
@respond_to(r'感謝|ありがとう|好き|すごい')
@write_log
def be_shy(message):
    message.reply('そんなこと言われたら照れるぱっちょ:denpaccho_upper_left::denpaccho_upper_right:')


def _get_user(message):
    return message.channel._client.users[message.body['user']]['name']


def _send_help(message, user):
    message.send('{user}くんはまだ設定をしていないみたいだね'.format(user=user))
    message.send('"@kintai-paccho 従業員コード 1234" のように入力するぱっちょ！')
    message.send('従業員コード とは King of Time にログインしたあとに自分の名前の左に出ている4桁の数字のことだよ！')


def _timerecord(message, record_type):
    if record_type == '出勤':
        code = 1
    elif record_type == '退勤':
        code = 2
    else:
        return False
    user = _get_user(message)
    employee_key = Employee.get_key(user)
    if not employee_key:
        _send_help(message, user)
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
