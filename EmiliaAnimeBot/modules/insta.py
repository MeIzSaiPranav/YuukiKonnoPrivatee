import aiohttp
from pyrogram import filters
from EmiliaAnimeBot import pgram as pbot
from EmiliaAnimeBot.pyrogramee.errors import capture_err


@pbot.on_message(filters.command('insta'))
@capture_err
async def instaa(_, message):
    if len(message.command) != 2:
        await message.reply_text("/insta Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://instagram.com/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**Info Of {name}**
**Full Name:** `{name}`
**UserName:** `{username}`
**Link:** [Here]({url})
**Posts Count:** `{company}`
**Category:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
