from telethon import events
import asyncio
from EmiliaAnimeBot.Cutiepiibot.py
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os

try:
 import subprocess
except:
 os.system("pip install instantmusic")



os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s "+name)

@saitama(outgoing=True, pattern="^/music(?: |$)(.*)")
async def getmusic(so):
    if so.fwd_from:
        return
    await so.client(JoinChannelRequest("t.me/PigasusSupport"))
    song = so.pattern_match.group(1)
    chat = "@SongsForYouBot"
    link = f"/song {song}"
    await so.edit("🔹Ok wait... 📡Searching your song🔸")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await so.edit("📥Downloading...Please wait🤙")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await so.edit("Please unblock @SongsForYouBot and try searching again🤐")
              return
          await so.edit("Ohh.. I got something!! Wait sending😋🤙")
          await asyncio.sleep(3)
          await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await so.delete()
