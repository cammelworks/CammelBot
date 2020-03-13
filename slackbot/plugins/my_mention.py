# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import re
from datetime import datetime
import locale

locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

@respond_to('time')
def now(message):
    strftime = datetime.now().strftime("%Y/%m/%d %H時%M分%S秒です")
    message.reply(strftime)

@respond_to('今何時')
def now_time(message):
    strftime = datetime.now().strftime("%Y/%m/%d %H時%M分%S秒です")
    message.reply(strftime)

@respond_to('あ')
def test(message):
    message.reply("test")

@default_reply()
def default(message):
    mes = message.body['text']
    message.reply(mes)