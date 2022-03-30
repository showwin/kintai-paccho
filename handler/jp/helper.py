def response_configuration_help(say):
    say("""
まだハッピー道具 kintai-paccho の設定をしていないみたいだっピね
"/employee-code 1234" のように入力するっピ！
King of Time にログインしたあとに画面右上の自分の名前の左に出ている数字やアルファベットを入力するっピ！
    """)


def response_kot_error(say, e: Exception):
    say('King of Time でエラーレスポンスが返ってきたっピ！')
    say(str(e))
