import datetime

import dateutil.relativedelta

from ..requester import KOTRequester
from .helper import get_employee_key, get_user


def help_holiday(message):
    user = get_user(message)
    message.send('有給の残日数を聞きたい場合は "@kintai-paccho 残休暇日数"'.format(user=user))
    message.send('有給の取得申請をする場合は "@kintai-paccho 2018年xx月xx日に有給取得したいです"'.format(user=user))
    message.send('と伝えてぱっちょ:denpacho_face_large:')


def get_remained_holiday_count(message):
    user = get_user(message)
    employee_key = get_employee_key(message)
    if not employee_key:
        return

    requester = KOTRequester()
    one_month_before = datetime.datetime.today() - dateutil.relativedelta.relativedelta(months=1)
    date_str = one_month_before.strftime('%Y-%m')
    resp = requester.get('/monthly-workings/holiday-remained/1000/{}'.format(date_str))
    remained_days = 0
    for record in resp:
        if employee_key == record['employeeKey']:
            remained_days = record['holidayRemained'][0]['day']
            break
    message.reply('{}くんの残休暇日数は{}日ぱっちょ:denpacho_face_large:'.format(user, remained_days))


def apply_holiday(message):
    try:
        apply_date_str = message.body['text'].split('に')[0]
        parsed_date = datetime.datetime.strptime(apply_date_str, '%Y年%m月%d日')
    except (IndexError, ValueError):
        message.reply('日付の形式が違うぱっちょ:exclamation: 2018年01月01日のように入力するぱっちょ:oni_paccho:')

    employee_key = get_employee_key(message)
    if not employee_key:
        return

    message.reply('ごめんね、King of TimeのAPIがアホだから今は有給申請できないぱっちょ:denpacho_face_large:')
