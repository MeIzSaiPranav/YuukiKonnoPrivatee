from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import OWNER_ID
from EmiliaAnimeBot import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont


@register(pattern="^/marsh_logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./EmiliaAnimeBot/resources/marshmallow.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 399
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./EmiliaAnimeBot/resources/Fast Hand.otf", 85)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(327, 222, 222))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="White", stroke_width=7, stroke_fill="Blue")
    fname2 = "LogoByYone.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Me_iz_mad_boi")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PigasusSupport, {e}')



   
@register(pattern="^/catto_logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./EmiliaAnimeBot/resources/catto.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./EmiliaAnimeBot/resources/NeonMachine-qwDV.ttf", 100)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "LogoByYone.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Me_iz_Mad_Boi")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PigasusSupport, {e}')
 
 
 

@register(pattern="^/hacker_logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./EmiliaAnimeBot/resources/hamcker.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 199
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./EmiliaAnimeBot/resources/Ok.ttf", 75)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.13)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/1, (image_heightz-h)/1), text, font=font, fill=(327, 222, 222))
    x = (image_widthz-w)/1
    y= ((image_heightz-h)/2+3)
    draw.text((x, y), text, font=font, fill="White", stroke_width=7, stroke_fill="Red")
    fname2 = "LogoByYone.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Me_iz_mad_boi")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PigasusSupport, {e}')




@register(pattern="^/marsho_logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./EmiliaAnimeBot/resources/marsh.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 399
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./EmiliaAnimeBot/resources/Marsh.otf", 85)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(327, 222, 222))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="White", stroke_width=7, stroke_fill="Green")
    fname2 = "LogoByYone.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Me_iz_mad_boi")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PigasusSupport, {e}')



  
@register(pattern="^/anime_logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./EmiliaAnimeBot/resources/Animeee.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 399
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./EmiliaAnimeBot/resources/LemonMilkitalic.otf", 85)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/1, (image_heightz-h)/2), text, font=font, fill=(327, 222, 222))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/1+6)
    draw.text((x, y), text, font=font, fill="White", stroke_width=7, stroke_fill="Red")
    fname2 = "LogoByYone.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Me_iz_mad_boi")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PigasusSupport, {e}')
 
 
 
 
@register(pattern="^/marshmallow ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./EmiliaAnimeBot/resources/marshmalloww.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 399
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./EmiliaAnimeBot/resources/CHERL___.TTF", 85)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/0), text, font=font, fill=(327, 222, 222))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="White", stroke_width=7, stroke_fill="Blue")
    fname2 = "LogoByYone.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Me_iz_mad_boi")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PigasusSupport, {e}')
 
 
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")



__help__ = """
 ❍ /marsh_logo text :  I'll Create Marshmello logo with your name
 ❍ /catto_logo text : I'll Create Catto logo with your name
 ❍/anime_logo text : i'll make a Anime logo With You Name
 ❍/marsho_logo text : i'll make a special marshmello logo with your name
 ❍/hacker_logo text : i'll make a hacker logo with you name 

_If You Use Caps In Command It Won't Work.
 """
__mod_name__ = "Logo"
