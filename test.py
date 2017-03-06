#!/usr/bin/env python
import time
import random
import datetime
import telepot

def bella(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command %s from %s' % (command, chat_id)

bot = telepot.Bot('*** INSERT TOKEN ***')
bot.message_loop(bella)
print 'I am listening ...'

## Keep server alive
while 1:
    time.sleep(10)
