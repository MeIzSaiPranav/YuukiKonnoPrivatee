from telethon import events, Button, custom
import re, os
import random
import datetime
import time
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from EmiliaAnimeBot import telethn as borg
from telethon.tl.types import ChannelParticipantsAdmins
from EmiliaAnimeBot import StartTime, dispatcher
import asyncio
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
edit_time = 10
"""=====================YUKKI====================="""
yukki1 = "https://telegra.ph/file/ae43f3254f76d0f7f9cf7.jpg"
yukki2 = "https://telegra.ph/file/0958215fe0ca611f2b7a3.jpg"
yukki3 = "https://telegra.ph/file/0e71b32cb9eb556b6833d.jpg"
yukki4 = "https://telegra.ph/file/749facab79add0d08d680.jpg"
"""=====================YUKKI====================="""

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    yukki = "**♡ I,m Yuuki💖**\n\n"
    yukki += "**♡ I'm Working Properly**\n\n"
    yukki += f"**♡ Yukki :** `{uptime}`\n\n"
    yukki += "**♡ My Master :** [Madboi](t.me/Me_Iz_mad_boi)`\n"
    yukki += "**♡ Telethon Version : 1.23.0**\n"
    BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
    on = await borg.send_file(yes.chat_id, file=yukki1,caption=yukki, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=yukki2, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=yukki3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=yukki1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=yukki3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=yukki2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=yukki1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=yukki4, buttons=BUTTON)

@register(pattern=("/myinfo"))
async def semx(event):
  await tbot.send_message(event.chat_id, f'**➢ Hᴇʏ {(event.sender.first_name)}**\n\n**➢ I Aᴍ [Yᴜᴜᴋɪ](t.me/YuukiKonnoRobot)**\n**➢ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Sᴀɪ](t.me/Me_Iz_Mad_Boi)**', file='cute.jpg', buttons=[Button.inline('**Iɴғᴏ**', data="sex"), Button.url('**Sᴜᴘᴘᴏʀᴛ**', 'https://t.me/YuukiSupportChat')], reply_to=event)
on = await borg.send_file(yes.chat_id, file=yukki1,caption=yukki, buttons=BUTTON)

 await asyncio.sleep(edit_time)
 ok = await borg.edit_message(yes.chat_id, on, file=yukki2, buttons=BUTTON) 
    
 await asyncio.sleep(edit_time)
 ok2 = await borg.edit_message(yes.chat_id, ok, file=yukki3, buttons=BUTTON)

 await asyncio.sleep(edit_time)
 ok3 = await borg.edit_message(yes.chat_id, ok2, file=yukki1, buttons=BUTTON)
    
 await asyncio.sleep(edit_time)
 ok4 = await borg.edit_message(yes.chat_id, ok3, file=yukki3, buttons=BUTTON)
    
 await asyncio.sleep(edit_time)
 ok5 = await borg.edit_message(yes.chat_id, ok4, file=yukki2, buttons=BUTTON)
    
 await asyncio.sleep(edit_time)
 ok6 = await borg.edit_message(yes.chat_id, ok5, file=yukki1, buttons=BUTTON)
    
 await asyncio.sleep(edit_time)
 ok7 = await borg.edit_message(yes.chat_id, ok6, file=yukki4, buttons=BUTTON)
    
@tbot.on(events.CallbackQuery(pattern=r"sex"))
async def ok(event):
     await event.answer(f'➢ Fɪʀsᴛ Nᴀᴍᴇ : {(event.sender.first_name)}\n➢ Lᴀsᴛ Nᴀᴍᴇ : {(event.sender.last_name)}\n➢ Usᴇʀɴᴀᴍᴇ : {(event.sender.username)}\n➢ Usᴇʀ Iᴅ : {(event.sender.id)}', alert=True)
