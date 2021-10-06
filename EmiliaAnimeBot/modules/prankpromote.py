import asyncio

from bs4 import *

from EmiliaAnimeBot.events import register


@register(pattern="ppromote")
async def ppromote (_, message):
    msg = await eor(ult, "**PROMOTING USER..**")
    await asyncio.sleep(1)
    await msg.edit("**PROMOTING USER...**")
    await asyncio.sleep(1)
    await msg.edit("**GIVING RIGHTS**")
    await asyncio.sleep(1)
    await msg.edit("**PROMOTED USER SUCCESSFULLY**")
