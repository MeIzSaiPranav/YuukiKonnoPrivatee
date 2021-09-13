import os
from EmiliaAnimeBot import telethn as tbot
from geopy.geocoders import Nominatim
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import *
from telethon import *
from telethon.tl import *

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@register(pattern="^/gps (.*)")
async def _(event):
    args = event.pattern_match.group(1)

    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
        gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
        await tbot.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(float(latitude), float(longitude))
            ),
        )
        await event.reply(
            "Open with: [🌏Google Maps]({})".format(gm),
            link_preview=False,
        )
    except Exception as e:
        print(e)
        await event.reply("I can't find that")

        
        
__help__ = """
 *See A Place's Map With The Help Of Google Map:*
  - /gps Chennai
  - /gps New York
 Usage: hahaha just a Gps.
 warning: Don't Use This Command Much Times.
"""

__mod_name__ = "Gps"
