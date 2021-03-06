from telegram import Update, Bot
from telegram.ext import run_async

from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler
from EmiliaAnimeBot import dispatcher

@run_async
def shout(bot: Bot, update: Update, args):
    if len(args) == 0:
        update.effective_message.reply_text("Where is text?")
        return

    msg = "```"
    text = " ".join(args)
    result = []
    result.append(' '.join([s for s in text]))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")
    
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, pass_args=True)

dispatcher.add_handler(SHOUT_HANDLER)
