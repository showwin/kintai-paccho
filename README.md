# kintai-paccho
Slackから勤怠入力するSlack Botだぱっちょ。

[KING OF TIME](https://www.kingtime.jp/) のみに対応しています。


## 事前準備
Slack Appの作成。  
参考: https://slack.dev/bolt-python/tutorial/getting-started

Socket Mode は ON にする
![](https://github.com/showwin/kintai-paccho/blob/master/doc/setup1.png)

必要な権限
![](https://github.com/showwin/kintai-paccho/blob/master/doc/setup2.png)
![](https://github.com/showwin/kintai-paccho/blob/master/doc/setup2-2.png)


Slash コマンドの登録
![](https://github.com/showwin/kintai-paccho/blob/master/doc/setup3.png)


## 起動方法

```
$ git clone git@github.com:showwin/kintai-paccho.git
$ cd kintai-paccho
$ export SLACK_BOT_TOKEN=xoxb-<your-bot-token>  # Slack の Token を設定
$ export SLACK_APP_TOKEN=xapp-<your-app-level-token>  # Slack の Token を設定
$ export KOT_TOKEN=xxxxxxxxxxxxxxxx  # King of Time の Token を設定
$ nohup python run.py &
```

supervisor などで監視すると良い良いと思います。

## botとの接し方

### Lv.0
登録する


### Lv.1
`おはー` と `おつー`  で出勤と退勤  

![](https://github.com/showwin/kintai-paccho/blob/master/doc/how_to_use_1.png)


### Lv.2
途中で休憩するとき

![](https://github.com/showwin/kintai-paccho/blob/master/doc/how_to_use_2.png)
![](https://github.com/showwin/kintai-paccho/blob/master/doc/how_to_use_3.png)


## 注意事項
可愛いアイコンたちは **著作権に違反しない範囲で** ご自身でご設定ください :pray:
