from Sophia.events import register
from Sophia import telethn as System
from PIL import Image, ImageDraw, ImageFont
import os

async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return replied_user

@register(pattern=("/get_id"))
async def image_maker(event) -> None:
    replied_user = await event.get_reply_message()
    # Download profile photo
    await System.download_profile_photo(
        replied_user.sender_id, file="user.png", download_big=True
    )
    user_photo = Image.open("user.png")
    # open id photo
    id_template = Image.open("ID.png")
    # resize user photo to fit box in id template
    user_photo = user_photo.resize((1159, 1241))
    # put image in position
    id_template.paste(user_photo, (1003, 641))
    # postion on where to draw text
    draw = ImageDraw.Draw(id_template)
    color = "rgb(0, 0, 0)"  # black
    font = ImageFont.truetype("font.ttf", size=80)
    font2 = ImageFont.truetype("font2.ttf", size=100)
    # put text in image
    draw.text(
        (1000, 460),
        replied_user.sender.first_name.replace("\u2060", ""),
        fill=color,
        font=font2,
    )
    draw.text((393, 50), str(replied_user.sender_id), fill=color, font=font)
    id_template.save("user_id.png")
    if "doc" in event.text:
        force_document = True
    else:
        force_document = False
    await System.send_message(
        event.chat_id,
        "Generated User ID",
        reply_to=event.message.id,
        file="user_id.png",
        force_document=force_document,
        silent=True,
    )
    os.remove("user_id.png")
