from ..employee import Employee
from ..requester import KOTException, KOTRequester
from .helper import get_user


def configure_employee(message):
    # 従業員コードを抜き出す
    user = get_user(message)
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
