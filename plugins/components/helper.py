from ..employee import Employee


def get_user(message):
    return message.channel._client.users[message.body['user']]['name']


def get_employee_key(message):
    user = get_user(message)
    employee_key = Employee.get_key(user)
    if not employee_key:
        _send_configuration_help(message, user)
        return None
    return employee_key


def _send_configuration_help(message, user):
    message.send('{user}くんはまだ設定をしていないみたいだね'.format(user=user))
    message.send('"@kintai-paccho 従業員コード 1234" のように入力するぱっちょ！')
    message.send('従業員コード とは King of Time にログインしたあとに自分の名前の左に出ている4桁の数字のことだよ！')
