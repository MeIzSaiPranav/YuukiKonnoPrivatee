from telethon import events, Button, custom
import re, os
import random
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
PHOTO = "https://telegra.ph/file/ae43f3254f76d0f7f9cf7.jpg"

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

 
@register(pattern=("/myinfo"))
async def semx(event):
  await tbot.send_message(event.chat_id, f'**➢ Hᴇʏ {(event.sender.first_name)}**\n\n**➢ I Aᴍ [Yᴜᴋɪɴᴀ](t.me/YuukiKonnoRobot)**\n**➢ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Sᴀɪ](t.me/Me_Iz_Mad_Boi)**', file='cute.jpg', buttons=[Button.inline('**Iɴғᴏ**', data="sex"), Button.url('**Sᴜᴘᴘᴏʀᴛ**', 'https://t.me/YuukiSupportChat')], reply_to=event)
  
@tbot.on(events.CallbackQuery(pattern=r"sex"))
async def ok(event):
     await event.answer(f'➢ Fɪʀsᴛ Nᴀᴍᴇ : {(event.sender.first_name)}\n➢ Lᴀsᴛ Nᴀᴍᴇ : {(event.sender.last_name)}\n➢ Usᴇʀɴᴀᴍᴇ : {(event.sender.username)}\n➢ Usᴇʀ Iᴅ : {(event.sender.id)}', alert=True)