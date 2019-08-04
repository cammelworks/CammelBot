# CammelBot
Slack Bot managing the schedule of daily scrum, sprints and so on.

## 課題
Slackの\reminder機能を用いいてデイリースクラムの通知をしていたが、デイリースクラムが無い日にもあり、不便だった。デイリースクラムがある日にのみ通知をさせたい。

※\reminderでは一度設定したリマインダーは編集できない


## 仕様
### 週の予定を決める際に入力
Ex)デイリースクラムの日程の入力
```
dailyscrum 8/1, 8/2, 8/5, 8/8
```
Ex)モブプロの日程、時間、場所の入力
```
mobpro 8/4, 18:00~21:00, メディセンセミナー室3 
```
### 入力した日の前日の23:00と当日の8:00に通知
Ex)7/31　23:00(8/1にデイリースクラムがある場合)
```
明日はデイリースクラムです。欠席の場合は参加できない場合は連絡をお願いします
```
Ex)8/1　8:00(8/1にデイリースクラムがある場合)
```
おはようございます！今日はデイリースクラムがありあます。昨日の進捗と参加可能かどうかを教えてください。
```
### 当日の参加者を9:00にお知らせ
Ex)参加者 Tyani, Katchu, Daigo の場合
```
本日の参加者はTyani, Katchu, Daigoです
```
