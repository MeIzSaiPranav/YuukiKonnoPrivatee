from EmiliaAnimeBot import telethn as tbot
from EmiliaAnimeBot.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from EmiliaAnimeBot import OWNER_ID
from EmiliaAnimeBot import TEMP_DOWNLOAD_DIRECTORY as path
from EmiliaAnimeBot import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime
water = './EmiliaAnimeBot/resources/photo_2021-10-03_13-46-33.jpg'
client = tbot

@register(pattern=r"^/send ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./EmiliaAnimeBot/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("No File Found!")


from AmeliaRobot.events import load_module
import asyncio
import os
from datetime import datetime
from pathlib import Path

@register(pattern="^/install")
async def install(event):
    if event.fwd_from:
        return
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "EmiliaAnimeBot/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.reply("Installed.... 👍\n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                k = await event.reply("**Error!**\n⚠️Cannot Install! \n📂 File not supported \n Or Pre Installed Maybe..😁",
                )
                await asyncio.sleep(2)
                await k.delete()
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()
