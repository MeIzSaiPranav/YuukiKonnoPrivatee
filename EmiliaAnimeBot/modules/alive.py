from telethon import events, Button, custom
import re, os
import random
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
from EmiliaAnimeBot import telethn as tgbot
PHOTO = random.choice(["https://telegra.ph/file/9ce5e51b9f4a531ea830b.jpg","https://telegra.ph//file/7f3ae4b9105c001e5ac59.jpg","https://telegra.ph//file/24df0a9ca50f11f8a3bc2.jpg","https://telegra.ph//file/a3545f201acb627a02bed.jpg","https://telegra.ph//file/dce0a6f265ab823053059.jpg"])
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m Yuuki💖** \n\n"
  PIKACHU += "**♡ I'm Working Properly**\n\n"
  PIKACHU += "**♡ Yuuki : 2.0 LATEST**\n\n"
  PIKACHU += "**♡ My Master :** [Madboi](t.me/Me_Iz_mad_boi)\n\n"
  PIKACHU += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
