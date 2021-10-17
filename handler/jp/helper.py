def response_configuration_help(say):
    say("""
まだ kintai-paccho の設定をしていないみたいだね
"/employee-code 1234" のように入力するぱっちょ！
King of Time にログインしたあとに画面右上の自分の名前の左に出ている4桁の数字を入力してね！
        """)

def response_kot_error(say, e: Exception):
    say('King of Time でエラーレスポンスが返ってきたぱっちょ！')
    say(str(e))
