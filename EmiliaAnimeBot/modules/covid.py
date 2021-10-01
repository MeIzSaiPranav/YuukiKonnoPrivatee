import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from EmiliaAnimeBot import dispatcher
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler


@run_async
def covid(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text.split(" ", 1)
    if len(text) == 1:
        r = requests.get("https://corona.lmao.ninja/v2/all").json()
        reply_text = f"**Global Totals** 🦠\nCases: {r['🥺cases']:,}\n😟Cases Today: {r['todayCases']:,}\n⚰️Deaths: {r['deaths']:,}\n⚰️Deaths Today: {r['todayDeaths']:,}\n😊Recovered: {r['recovered']:,}\n😔Active: {r['active']:,}\n⚠️Critical: {r['critical']:,}\nCases/Mil: {r['casesPerOneMillion']}\nDeaths/Mil: {r['deathsPerOneMillion']}"
    else:
        variabla = text[1]
        r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
        reply_text = f"**Cases for {r['country']} 🦠**\nCases: {r['cases']:,}\n😟Cases Today: {r['todayCases']:,}\n⚰️Deaths: {r['deaths']:,}\n⚰️Deaths Today: {r['todayDeaths']:,}\n😊Recovered: {r['recovered']:,}\n😔Active: {r['active']:,}\n⚠️Critical: {r['critical']:,}\nCases/Mil: {r['casesPerOneMillion']}\nDeaths/Mil: {r['deathsPerOneMillion']}"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid)
dispatcher.add_handler(COVID_HANDLER)

mod_name = "Covid-19"

help = """
~ /covid** <songname artist(optional)>: download the song in it's best quality available.(API BASED)
Commands     
- /covid - To Get Global Stats of Covid.
- /covid [Country] - To Get Stats of A Single Country.
- /corona - Same as `/covid 
"""
