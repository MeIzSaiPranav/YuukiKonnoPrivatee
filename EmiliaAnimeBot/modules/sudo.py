import html

from typing import List

from telegram import Update, Bot
from telegram.ext import CommandHandler, Filters
from telegram.ext.dispatcher import run_async

from EmiliaAnimeBot import dispatcher, DRAGONS, OWNER_USERNAME, OWNER_ID
from EmiliaAnimeBot.modules.helper_funcs.extraction import extract_user
from EmiliaAnimeBot.modules.helper_funcs.chat_status import bot_admin


@bot_admin
@run_async
def sudopromote(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    banner = update.effective_user
    user_id = extract_user(message, args)
    
    if not user_id:
        message.reply_text("You don't seem to be referring to a user.")
        return ""
        
    if int(user_id) == OWNER_ID:
        message.reply_text("The specified user is my owner! No need add him to DRAGONS list!")
        return ""
        
    if int(user_id) in DRAGONS:
        message.reply_text("The user is already a sudo user.")
        return ""
    
    with open("DRAGONS.txt","a") as file:
        file.write(str(user_id) + "\n")
    
    DRAGONS.append(user_id)
    message.reply_text("Succefully added to SUDO user list!")
        
    return ""

@bot_admin
@run_async
def sudodemote(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    user_id = extract_user(message, args)
    
    if not user_id:
        message.reply_text("You don't seem to be referring to a user.")
        return ""

    if int(user_id) == OWNER_ID:
        message.reply_text("The specified user is my owner! I won't remove him from DRAGONS list!")
        return ""
    
    if user_id not in DRAGONS:
        message.reply_text("{} is not a sudo user".format(user_id))
        return ""

    users = [line.rstrip('\n') for line in open("DRAGONS.txt")]

    with open("DRAGONS.txt","w") as file:
        for user in users:
            if not int(user) == user_id:
                file.write(str(user) + "\n")

    DRAGONS.remove(user_id)
    message.reply_text("Succefully removed from SUDO user list!")
    
    return ""


SUDOPROMOTE_HANDLER = CommandHandler("sudopromote", sudopromote, pass_args=True, filters=Filters.user(OWNER_ID))
SUDODEMOTE_HANDLER = CommandHandler("sudodemote", sudodemote, pass_args=True, filters=Filters.user(OWNER_ID))

dispatcher.add_handler(SUDOPROMOTE_HANDLER)
dispatcher.add_handler(SUDODEMOTE_HANDLER)
