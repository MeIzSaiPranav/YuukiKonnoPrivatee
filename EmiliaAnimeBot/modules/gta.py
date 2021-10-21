import os
import requests

from EmiliaAnimeBot.events import register
from EmiliaAnimeBot.pyrogramee.pluginshelper
from EmiliaAnimeBot import telethn as gta

from telegraph import upload_file


@register(pattern=("/wasted"))
   
async def wasted(client, message):
    gta = await edit_or_reply(message, "`Processing`")
    if not message.reply_to_message:
        await gta.edit("`Reply to a photo :(`")
        return
    ok = message.reply_to_message
    pic = await client.download_media(ok)
    poto_url = upload_file(pic)
    imglink = f"https://telegra.ph{poto_url[0]}"
    
    url = f"https://some-random-api.ml/canvas/wasted?avatar={imglink}"
   
    await client.send_photo(
        message.chat.id,
        url,
        reply_to_message_id=message.reply_to_message.message_id,
    )
    await gta.delete()
    os.remove(pic)
