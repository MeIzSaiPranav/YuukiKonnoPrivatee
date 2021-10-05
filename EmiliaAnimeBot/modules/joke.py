import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler

JOKE_STRINGS = (
    "மழை வந்ததும் கவிதை வந்தால் அவன் கவிஞன். அதுவே காயப்போட்ட துணி ஞாபகத்திற்கு வந்தால் அவன் தான் குடும்பஸ்தன்.",
    "மகன்களை பெற்ற அம்மாவுக்கு மட்டுமே தெரியும். அவனை மளிகை கடைக்கு அனுப்புனா. மீதி காசு கைக்கு வராது என்று."
	)

@run_async
def joke(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(JOKE_STRINGS))
    else:
      message.reply_text(random.choice(JOKE_STRINGS))
	  

JOKE_HANDLER = DisableAbleCommandHandler("joke", joke)

dispatcher.add_handler(JOKE_HANDLER)
