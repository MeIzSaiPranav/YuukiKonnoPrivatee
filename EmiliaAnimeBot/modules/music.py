import io
import os

import lyricsgenius
from pyrogram import filters
from tswift import Song

from EmiliaAnimeBot.config import get_str_key
from EmiliaAnimeBot.services.pyrogram import pbot

GENIUS = get_str_key("GENIUS_API_TOKEN", None)


# Lel, Didn't Get Time To Make New One So Used Plugin Made br @mrconfused and @sandy1709 dont edit credits


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics.....")
    query = message.text
    if not query:
        await lel.edit("`What I am Supposed to find `")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! try with artist name along with song if still doesnt work try `.glyrics`"
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work try `.glyrics`"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply


@pbot.on_message(filters.command(["glyric", "glyrics"]))
async def lyrics(client, message):

    if r"-" in message.text:
        pass
    else:
        await message.reply(
            "`Error: please use '-' as divider for <artist> and <song>`\n"
            "eg: `.glyrics Nicki Minaj - Super Bass`"
        )
        return

    if GENIUS is None:
        await message.reply(
            "`Provide genius access token to config.py or Heroku Config first kthxbye!`"
        )
    else:
        genius = lyricsgenius.Genius(GENIUS)
        try:
            args = message.text.split(".lyrics")[1].split("-")
            artist = args[0].strip(" ")
            song = args[1].strip(" ")
        except Exception:
            await message.reply("`Lel please provide artist and song names`")
            return

    if len(args) < 1:
        await message.reply("`Please provide artist and song names`")
        return

    lel = await message.reply(f"`Searching lyrics for {artist} - {song}...`")

    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None

    if songs is None:
        await lel.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await lel.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await client.send_document(
            message.chat.id,
            "lyrics.txt",
            reply_to_msg_id=message.message_id,
        )
        os.remove("lyrics.txt")
    else:
        await lel.edit(
            f"**Search query**: \n`{artist} - {song}`\n\n```{songs.lyrics}```"
        )
    return
