import random

from telethon import events

from NekoRobot import tbot as neko


@register(pattern="^/wish ?(.*)")
async def wish(e):
    quew = event.pattern_match.group(1)
    if event.sender_id != OWNER_ID and not quew:
        await event.reply
            "Friend, please give me some text to say how many that text have chance!\nExample `/wish <I want a chocolate>`"

    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://te.legra.ph/file/79b3c7bfa241a0e4c9fdd.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.💜**\n\n__chance of success {mm}%__",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = "https://te.legra.ph/file/79b3c7bfa241a0e4c9fdd.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.💜**\n\n__chance of success {mm}%__",
            reply_to=e,
        )
