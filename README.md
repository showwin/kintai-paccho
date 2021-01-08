# kintai-paccho
Slackから勤怠入力するSlack Botだぱっちょ。

[KING OF TIME](https://www.kingtime.jp/) のみに対応しています。


## 使い方

```
$ git clone git@github.com:showwin/kintai-paccho.git
$ cd kintai-paccho
$ export SLACK_TOKEN_KINTAI_PACCHO=xxxxxxxxxxxxxxxx  # Slack の Token を設定
$ export KOT_TOKEN=xxxxxxxxxxxxxxxx  # King of Time の Token を設定
$ nohup python run.py &
```

## botとの接し方

### Lv.0
登録する

![](https://github.com/showwin/kintai-paccho/blob/master/doc/setup0.jpg)

![](https://github.com/showwin/kintai-paccho/blob/master/doc/setup1.jpg)

### Lv.1
`おはー` と `店じまい` (or `おつー` ) で出勤と退勤  
( `おはー` `店じまい` `おつー` は `@メンション` を飛ばさなくても反応してくれます)

![](https://github.com/showwin/kintai-paccho/blob/master/doc/image0.png)

![](https://github.com/showwin/kintai-paccho/blob/master/doc/image1.png)

![](https://github.com/showwin/kintai-paccho/blob/master/doc/image2.png)

### Lv.2
途中で休憩を挟みたいとき

![](https://github.com/showwin/kintai-paccho/blob/master/doc/image3.png)

![](https://github.com/showwin/kintai-paccho/blob/master/doc/image4.png)

### Lv.3
残り有給日数を確認する

![](https://github.com/showwin/kintai-paccho/blob/master/doc/image5.png)

## 注意事項
可愛いアイコンたちは **著作権に違反しない範囲で** ご自身でご設定ください :pray:
