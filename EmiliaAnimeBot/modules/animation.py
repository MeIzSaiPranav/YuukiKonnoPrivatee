import time

from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
from EmiliaAnimeBot.modules.helper_funcs.chat_status import user_admin
from telegram import Update
from telegram.ext import CallbackContext, run_async

#sleep how many times after each edit in 'onichan'
EDIT_SLEEP = 2
#edit how many times in 'onichan'
EDIT_TIMES = 5

EDIT_TIMES_KILL = 2

POLICE_SIREN = [
    "π΄π΄π΄β¬οΈβ¬οΈβ¬οΈπ΅π΅π΅\nπ΄π΄π΄β¬οΈβ¬οΈβ¬οΈπ΅π΅π΅\nπ΄π΄π΄β¬οΈβ¬οΈβ¬οΈπ΅π΅π΅",
    "π΅π΅π΅β¬οΈβ¬οΈβ¬οΈπ΄π΄π΄\nπ΅π΅π΅β¬οΈβ¬οΈβ¬οΈπ΄π΄π΄\nπ΅π΅π΅β¬οΈβ¬οΈβ¬οΈπ΄π΄π΄"
]

LOVE_EMOJY = [
    "β€οΈπ§‘β€οΈπβ€οΈπβ€οΈπ\nβ€οΈπβ€οΈπβ€οΈπβ€οΈπ§‘\nβ€οΈπ§‘β€οΈπβ€οΈπβ€οΈπ",
    "πβ€οΈππππππ§‘\nπ§‘β€οΈπβ€οΈπβ€οΈπβ€οΈ\nπβ€οΈπβ€οΈπβ€οΈπ§‘β€οΈ"
]

KILL_STRING = [
    "Pathetic Human DieπΏ!\n\n(γο½₯ΰΈ΄Οο½₯ΰΈ΄)οΈ»γβδΈ-->\n\n------>\n\n----------->",
    "---->\n\n(οΏ£γΌοΏ£) DEADππ\n\n\nUwU user killed successful!\n\n*happy noisesππ*"
]

@user_admin
@run_async
def onichan(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_text('onichan onichan police is coming!')
    for x in range(EDIT_TIMES):
        msg.edit_text(POLICE_SIREN[x % 2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('onichan , you are under arrest!')

@run_async
def love(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_text('checking love')
    for x in range(EDIT_TIMES):
        msg.edit_text(LOVE_EMOJY[x % 2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('True Love!')

@run_async
def kill(update: Update, context: CallbackContext):
    msg = update.effective_message.reply_text('getting my gunπΏπΏ.')
    for x in range(EDIT_TIMES_KILL):
        msg.edit_text(KILL_STRING[x % 2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('UwU Target killed successfullyπ!\n\n\n*Happy noisesππ*')

__help__ = """
β’ `/onichan`*:* Sends a police to arrest your onichan. 
β’ `/kill`*:* Kills the targeted person with a animated gun.
"""

ONICHAN_HANDLER = DisableAbleCommandHandler("onichan", onichan)
LOVE_HANDLER = DisableAbleCommandHandler("love", love)
KILL_HANDLER = DisableAbleCommandHandler ("kill", kill)
dispatcher.add_handler(ONICHAN_HANDLER)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(KILL_HANDLER)

__mod_name__ = "Animation"
__command_list__ = ["onichan", "love", "kill"]
__handlers__ = [ONICHAN_HANDLER , LOVE_HANDLER , KILL_HANDLER]
