from telethon import events, Button, custom
import re, os
import random
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph//file/7f3ae4b9105c001e5ac59.jpg"
file2 = "https://telegra.ph//file/a3545f201acb627a02bed.jpg"
file3 = "https://telegra.ph/file/53793cb19c971ee6868a5.jpg"
file4 = "https://telegra.ph/file/408ab930c9dec34367590.jpg"
""" =======================CONSTANTS====================== """

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
async def awake(event):
  current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m Yuuki💖** \n\n"
  PIKACHU += "**♡ I'm Working Properly**\n\n"
  PIKACHU += "**♡ Yuuki : 2.0 LATEST**\n\n"
  PIKACHU += "**♡ UPTIME : `{uptime}`\n\n"
  PIKACHU += "**♡ My Master :** [Madboi](t.me/Me_Iz_mad_boi)\n\n"
  PIKACHU += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
 on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    
 
@register(pattern=("/myinfo"))
async def semx(event):
  await tbot.send_message(event.chat_id, f'**➢ Hᴇʏ {(event.sender.first_name)}**\n\n**➢ I Aᴍ [Yᴜᴜᴋɪ](t.me/YuukiKonnoRobot)**\n**➢ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Sᴀɪ](t.me/Me_Iz_Mad_Boi)**', file='cute.jpg', buttons=[Button.inline('**Iɴғᴏ**', data="sex"), Button.url('**Sᴜᴘᴘᴏʀᴛ**', 'https://t.me/YuukiSupportChat')], reply_to=event)
  
@tbot.on(events.CallbackQuery(pattern=r"sex"))
async def ok(event):
     await event.answer(f'➢ Fɪʀsᴛ Nᴀᴍᴇ : {(event.sender.first_name)}\n➢ Lᴀsᴛ Nᴀᴍᴇ : {(event.sender.last_name)}\n➢ Usᴇʀɴᴀᴍᴇ : {(event.sender.username)}\n➢ Usᴇʀ Iᴅ : {(event.sender.id)}', alert=True)
