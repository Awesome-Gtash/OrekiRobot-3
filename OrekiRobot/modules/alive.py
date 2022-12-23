import asyncio
import datetime
from datetime import datetime

from pyrogram import __version__ as pyrover
from telethon import Button
from telegram import __version__ as ptb
from telethon import __version__ as tlhver

from OrekiRobot import BOT_NAME
from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

edit_time = 5
""" =======================oreki====================== """
file1 = "https://te.legra.ph/file/e3a37df24dd0965dba2cf.jpg"
file2 = "https://te.legra.ph/file/0de0f032e682c031f17d9.jpg"
file3 = "https://te.legra.ph/file/283d0016973127a7f6cbf.jpg"
file4 = "https://te.legra.ph/file/964030fa52d6dcc53fe4d.jpg"
file5 = "https://te.legra.ph/file/d64efaf679941b87b1341.jpg"
""" =======================oreki====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    oreki += f"**♡ Hola I'm {BOT_NAME}!**\n\n"
    oreki += f"**♡ My Uptime ~ 🖤:** `{uptime}`\n\n"
    oreki += f"**♡ Python-telegram-bot Version ~ 🖤 :** `{ptb}`\n\n"
    oreki += f"**♡ Telethon Version ~ 🖤:** `{tlhver}`\n\n"
    oreki += f"**♡ Pyrogram Version ~ 🖤:** `{pyrover}`\n\n"
    oreki += f"**♡ My Master ~ 🖤 :** [The Gtash](https://t.me/Awesome_Gtashxd)"
    BUTTON = [
        [
            Button.url("【► Updates ◄】", f"https://t.me/Dev_Updates"),
            Button.url("【► Support ◄】", f"https://t.me/Dev_SupportChat"),
        ]
    ]
    on = await oreki.send_file(yes.chat_id, file=file2, caption=Oreki, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await oreki.edit_message(yes.chat_id, on, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok2 = await oreki.edit_message(yes.chat_id, ok, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await oreki.edit_message(yes.chat_id, ok2, file=file1, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok4 = await oreki.edit_message(yes.chat_id, ok3, file=file2, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await oreki.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok6 = await oreki.edit_message(yes.chat_id, ok5, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok7 = await oreki.edit_message(yes.chat_id, ok6, file=file4, buttons=BUTTON)
