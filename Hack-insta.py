from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon import TelegramClient, sync
from telethon import events
from telethon.tl.custom import Button
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from bs4 import BeautifulSoup
import time
import re, threading
from time import sleep
c = requests.session()
def css():
	api_id = '2192036'
	api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
	client = TelegramClient('session', api_id, api_hash)
	client.start()
	bot_user = '@qweqwe1919bot'
	channel_entity = client.get_entity(bot_user)
	client.send_message('qweqwe1919bot' ,'/start')
	sleep(2)
	mssag = client.get_messages('qweqwe1919bot', limit=1)
	mssag[0].click(2)
	sleep(10)
	mssag1 = client.get_messages('qweqwe1919bot', limit=1)
	mssag1[0].click(0)
	sleep(5)
	for ffguf  in range(10000):
	    sleep(10)
	    l = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	    j = l.messages[0]
	    if j.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	        client.send_message('me','مافي قنوات بعد')
	        break
	    url = j.reply_markup.rows[0].buttons[0].url
	    try :
	        try :
	           client(JoinChannelRequest(url))
	        except :
	            bott = url.split('/')[-1]
	            client(ImportChatInviteRequest(bott))
	
	        mssag2 = client.get_messages('qweqwe1919bot', limit=1)
	        mssag2[0].click(text='تحقق')
	    except :
	        client.send_message('me','حسابك انحضر استاذ ✅🌝 @DTDTDT ')
	        break
	client.disconnect()



css()
