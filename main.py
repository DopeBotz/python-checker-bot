#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= "5689646", #get it from https://my.telegram.org/auth
    api_hash="895de5ae804308803c19814afabb0de7", #get it from https://my.telegram.org/auth
    bot_token="5205589679:AAEAbJ2C5L4G1PbDW0DC778Ks8BYx3CqI0Q", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
