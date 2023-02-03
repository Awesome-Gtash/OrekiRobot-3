import random

from telethon import events

from OrekiRobot import tbot as oreki


@oreki.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):

    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://te.legra.ph/file/79b3c7bfa241a0e4c9fdd.jpg"
        await oreki.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey My Friend, [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.🖤**\n\n__chance of success {mm}%__",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = "https://te.legra.ph/file/79b3c7bfa241a0e4c9fdd.jpg"
        await oreki.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey My Friend, [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.🖤**\n\n__chance of success {mm}%__",
            reply_to=e,
        )
