import datetime
import functools
import json
import time

from slackbot.bot import listen_to, respond_to

from .employee import Employee
from .logger import write_log
from .requester import KOTException, KOTRequester


# Decorator
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


@listen_to('^おはー$')
@respond_to('^おはー$')
@write_log
def start_timerecord(message):
    if _timerecord(message, '出勤'):
        message.send(':den_paccho1: < おはー　だこくしたよ〜')


@listen_to('^店じまい$')
@respond_to('^店じまい$')
@listen_to('^おつー$')
@respond_to('^おつー$')
@write_log
def end_timerecord(message):
    if _timerecord(message, '退勤'):
        message.send(':gas_paccho_1: < おつー　打刻したよー')


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
