from telethon import events, Button, custom
import re, os
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
from EmiliaAnimeBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/9ce5e51b9f4a531ea830b.jpg"
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
