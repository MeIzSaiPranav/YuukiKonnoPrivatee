from telegram import Update
from telegram.ext import CallbackContext, run_async

from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler

EHI_STRINGS = "Here, new ehi files by @YuukiKonnoRobot 👸\n\n👉 https://da.gd/OhPiHf"


@run_async
def ehi(update: Update, context: CallbackContext):
    update.effective_message.reply_text(EHI_STRINGS)


EHI_HANDLER = DisableAbleCommandHandler("ehi", ehi)
dispatcher.add_handler(EHI_HANDLER)
