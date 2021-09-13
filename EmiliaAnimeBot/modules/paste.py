import requests
from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


PASTED_IMG = "https://telegra.ph/file/207eaf3bdce8c267677ed.jpg"


@run_async
def paste(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text

    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]

    else:
        message.reply_text("What am I supposed to do with this?")
        return

    key = requests.post(
        'https://nekobin.com/api/documents', json={
            "content": data
        }).json().get('result').get('key')

    url = f'https://nekobin.com/{key}'

    reply_text = f'Pasted to NekoBin!'


    message.reply_photo(
        PASTED_IMG, caption=reply_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup = InlineKeyboardMarkup(
            [
                InlineKeyboardButton(text="Link", url={url})
            ]
        )
        )


PASTE_HANDLER = DisableAbleCommandHandler("paste", paste)
dispatcher.add_handler(PASTE_HANDLER)

__command_list__ = ["paste"]
__handlers__ = [PASTE_HANDLER]
__help__ = """
 • `/paste` *:* Saves replied content to `nekobin.com` and replies with a url
"""
__mod_name__ = "Paste"
