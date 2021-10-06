import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler


@run_async
def aniquote(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text.split(" ", 1)
    if len(text) == 1:
        r = requests.get("https://animechan.vercel.app/api/random").json()
        reply_text = f"**{resp['quote']}**\n
