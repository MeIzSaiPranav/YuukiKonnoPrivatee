from telegram.ext import run_async

from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
from EmiliaAnimeBot.modules.helper_funcs.alternate import send_message
from EmiliaAnimeBot.modules.helper_funcs.chat_status import user_admin


@run_async
@user_admin
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
command_list = ["snd"]
handlers = [ADD_CCHAT_HANDLER]
