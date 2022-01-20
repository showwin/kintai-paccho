import datetime
import re

from components.requester import KOTException
from components.typing import SlackRequest
from components.usecase import register_user, update_user_timezone
from handler.jp.helper import response_kot_error

TIMEZONE_REGEX = r'^(?:Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])$'

def register_employee_code(say, request: SlackRequest):
    if not _can_register():
        say('[08:30 ～ 10:00, 17:30 ～ 18:30] の時間帯はAPIの都合で勤怠登録しかできないんだ。ごめん:paccho:')
        return
    if not request.text:
        say('従業員コードが読み取れなかったよ')
        say('"/employee-code 1234" のように入力するぱっちょ！')
        return

    try:
        kot_username = register_user(request.user_id, request.text)
        say('{last_name} {first_name}さんの設定が完了したぱっちょ！'.format(
            last_name=kot_username['last_name'],
            first_name=kot_username['first_name']
        ))
    except KOTException as e:
        response_kot_error(say, e)


def set_timezone(say, request: SlackRequest):
    if not request.text or not _valid_timezone(request.text):
        say('タイムゾーンが読み取れなかったよ')
        say('"/set-timezone +09:00" のように入力するぱっちょ！')
        return

    update_user_timezone(request.user_id, request.text)
    say(f'タイムゾーンを {request.text} に設定したぱっちょ！')

def _can_register():
    time_now_str = datetime.datetime.now().strftime('%H%M')
    return not ('0830' < time_now_str < '1000' or '1730' < time_now_str < '1830')

def _valid_timezone(timezone):
    return bool(re.match(TIMEZONE_REGEX, timezone))
