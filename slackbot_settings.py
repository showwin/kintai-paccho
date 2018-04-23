import os

# botアカウントのトークンを指定
API_TOKEN = os.environ.get('SLACK_TOKEN_KINTAI_PACCHO')

# King of Time のトークンを設定
# KOT_TOKEN = os.environ.get('KOT_TOKEN')  @plugins/requester.py

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
HOW_TO_USE = """
わたしに向かって "おはー" か "店じまい" っていうぱっちょ！
"""
DEFAULT_REPLY = HOW_TO_USE

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
