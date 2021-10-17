import datetime

from components.requester import KOTException
from components.typing import SlackRequest
from components.usecase import register_user
from handler.jp.helper import response_kot_error


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


def _can_register():
    time_now_str = datetime.datetime.now().strftime('%H%M')
    return not ('0830' < time_now_str < '1000' or '1730' < time_now_str < '1830')
