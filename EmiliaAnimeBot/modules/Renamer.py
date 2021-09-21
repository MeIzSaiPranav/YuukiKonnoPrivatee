import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from EmiliaAnimeBot import DOWNLOAD_LOCATION
else:
    from EmiliaAnimeBot import DOWNLOAD_LOCATION

# the Strings used for this "thing"
import pyrogram

from EmiliaAnimeBot.utils.anydl_trans import Translation

logging.getLogger("pyrogram").setLevel(logging.WARNING)

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

# https://stackoverflow.com/a/37631799/4723940
from PIL import Image

from EmiliaAnimeBot import pgram as bot
from EmiliaAnimeBot.utils.chatbase import TRChatBase
from EmiliaAnimeBot.utils.display_progress import progress_for_pyrogram


@bot.on_message(pyrogram.filters.command(["rename"]))
async def rename_doc(bot, update):

    TRChatBase(update.from_user.id, update.text, "rename")
    if (" " in update.text) and (update.reply_to_message is not None):
        cmd, file_name = update.text.split(" ", 1)
        description = Translation.CUSTOM_CAPTION_UL_FILE
        download_location = DOWNLOAD_LOCATION + "/"
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id,
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(Translation.DOWNLOAD_START, a, c_time),
        )
        if the_real_download_location is not None:
            await bot.edit_message_text(
                text=Translation.SAVED_RECVD_DOC_FILE,
                chat_id=update.chat.id,
                message_id=a.message_id,
            )
            if "IndianMovie" in the_real_download_location:
                await bot.edit_message_text(
                    text=Translation.RENAME_403_ERR,
                    chat_id=update.chat.id,
                    message_id=a.message_id,
                )
                return
            new_file_name = download_location + file_name
            os.rename(the_real_download_location, new_file_name)
            await bot.edit_message_text(
                text=Translation.UPLOAD_START,
                chat_id=update.chat.id,
                message_id=a.message_id,
            )
            logger.info(the_real_download_location)
            thumb_image_path = (
                DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            )
            if not os.path.exists(thumb_image_path):
                thumb_image_path = None
            else:
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                # resize image
                # ref: https://t.me/PyrogramChat/44663
                # https://stackoverflow.com/a/21669827/4723940
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                # https://stackoverflow.com/a/37631799/4723940
                # img.thumbnail((90, 90))
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")
                # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
            c_time = time.time()
            await bot.send_document(
                chat_id=update.chat.id,
                document=new_file_name,
                thumb=thumb_image_path,
                caption=description,
                # reply_markup=reply_markup,
                reply_to_message_id=update.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(Translation.UPLOAD_START, a, c_time),
            )
            try:
                os.remove(new_file_name)
                os.remove(thumb_image_path)
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id=update.chat.id,
                message_id=a.message_id,
                disable_web_page_preview=True,
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.REPLY_TO_DOC_FOR_RENAME_FILE,
            reply_to_message_id=update.message_id,
        )
