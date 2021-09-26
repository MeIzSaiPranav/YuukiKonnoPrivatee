from requests import get
from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler
from EmiliaAnimeBot import dispatcher

link = 'https://raw.githubusercontent.com/davinash97/magisk_files/'

def magisk(update, context):
    magisk_dict = {
            "*Stable*": "master/stable.json", "\n"
            "*Beta*": "master/beta.json", "\n"
            "*Canary*": "canary/canary.json",
        }
    
    releases = '*Latest Magisk Releases:*\n\n'
    for magisk_type, release_url in magisk_dict.items():
        data = get(link + release_url).json()
        releases += f'{magisk_type}:\n' \
                    f'》 *Installer* - [Zip v{data["magisk"]["version"]}]({data["magisk"]["link"]}) \n' \
                    f'》 *Manager* - [App v{data["app"]["version"]}]({data["app"]["link"]}) \n' \
                    f'》 *Uninstaller* - [Uninstaller v{data["magisk"]["version"]}]({data["uninstaller"]["link"]}) \n'
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text=releases,
                             parse_mode=ParseMode.MARKDOWN,
                             disable_web_page_preview=True)
                             
magisk_handler = CommandHandler(['magisk', 'root', 'su'], magisk)
dispatcher.add_handler(magisk_handler)
