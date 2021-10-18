from telethon import events, Button, custom
import re, os
import random
import asyncio
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
"""=====================LOL====================="""
PHOTO = "https://telegra.ph/file/ae43f3254f76d0f7f9cf7.jpg"
fuck = "https://telegra.ph//file/7f3ae4b9105c001e5ac59.jpg"
sex = "https://telegra.ph//file/24df0a9ca50f11f8a3bc2.jpg"
lmao = "https://telegra.ph//file/a3545f201acb627a02bed.jpg"
lmao2 = "https://telegra.ph//file/dce0a6f265ab823053059.jpg"

"""================LOL=========================="""
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m Yuuki💖** \n\n"
  PIKACHU += "**♡ I'm Working Properly**\n\n"
  PIKACHU += "**♡ Yuuki : 2.0 LATEST**\n\n"
  PIKACHU += "**♡ My Master :** [Madboi](t.me/Me_Iz_mad_boi)\n\n"
  PIKACHU += "**♡ Telethon Version : 1.23.0**\n\n"
  
  on = await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
  await asyncio.sleep(5)
  ok = await event.edit_message(yes.chat_id, on, file=fuck, buttons=BUTTON) 

  await asyncio.sleep(5)
  ok2 = await event.edit_message(yes.chat_id, ok, file=sex, buttons=BUTTON)

  await asyncio.sleep(5)
  ok3 = await event.edit_message(yes.chat_id, ok2, file=lmao, buttons=BUTTON)
    
  await asyncio.sleep(5)
  ok4 = await event.edit_message(yes.chat_id, ok3, file=lmao2, buttons=BUTTON)
 
@register(pattern=("/myinfo"))
async def semx(event):
  await tbot.send_message(event.chat_id, f'**➢ Hᴇʏ {(event.sender.first_name)}**\n\n**➢ I Aᴍ [Yᴜᴜᴋɪ](t.me/YuukiKonnoRobot)**\n**➢ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Sᴀɪ](t.me/Me_Iz_Mad_Boi)**', file='cute.jpg', buttons=[Button.inline('**Iɴғᴏ**', data="sex"), Button.url('**Sᴜᴘᴘᴏʀᴛ**', 'https://t.me/YuukiSupportChat')], reply_to=event)
  
@tbot.on(events.CallbackQuery(pattern=r"sex"))
async def ok(event):
     await event.answer(f'➢ Fɪʀsᴛ Nᴀᴍᴇ : {(event.sender.first_name)}\n➢ Lᴀsᴛ Nᴀᴍᴇ : {(event.sender.last_name)}\n➢ Usᴇʀɴᴀᴍᴇ : {(event.sender.username)}\n➢ Usᴇʀ Iᴅ : {(event.sender.id)}', alert=True)
