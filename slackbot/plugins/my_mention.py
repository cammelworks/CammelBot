# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import re
from datetime import datetime
import locale

locale.setlocale(locale.LC_CTYPE, '')

@respond_to('time')
def now(message):
    strftime = datetime.now().strftime("%Y/%m/%d %H時%M分%S秒です")
    message.reply(strftime)

@respond_to('今何時')
def now_time(message):
    strftime = datetime.now().strftime("%Y/%m/%d %H時%M分%S秒です")
    message.reply(strftime)

@respond_to('MTG', re.IGNORECASE)
def mtg(message):
    message.send("<!channel> リマインド\n本日18:30からMTGです〜\n`本日のアジェンダ`はスレッドで\n報告等あるひとはお願いしま〜す:カニちゃん:")

@listen_to('いる??')
def here(message):
    message.reply("ここだよ!!メェェ〜")

@default_reply()
def default(message):
    mes = message.body['text']
    message.reply(mes)