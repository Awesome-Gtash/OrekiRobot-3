from pyrogram import __version__ as pyrover
from telethon import Button
from telegram import __version__ as ptb
from telethon import __version__ as tlhver

from OrekiRobot import BOT_NAME
from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as oreki

IMAGE = "https://te.legra.ph/file/344cdfc69c65647c10313.jpg"


@oreki(pattern=("/alive"))
async def awake(event):
    OREKI = """
**Hola I'm {BOT_NAME} ~ 🖤!**
**My Uptime ~ 🖤:** `{}`\n\n
**Python-Telegram-Bot Version ~ 🖤 :** `{ptb}`\n\n
**Telethon Version ~ 🖤:** `{tlhver}`\n\n
**Pyrogram Version ~ 🖤:** `{pyrover}`\n\n
**My Master ~ 🖤 :** [THE GTASH](https://t.me/Awesome_Gtashxd)
"""

    BUTTON = [
        [
            Button.url(
                "Add {BOT_NAME} To Your Group ✅", "https://t.me/{BOT_NAME}?startgroup=true"
            ),
    ],
    [
            Button.url(
                "Developer🎗", "https://t.me/Awesome_Gtashxd"
            ),
    ],
    [
            Button.url(
                "Support🎯", "https://t.me/Gtash_Association"
         ),
     ],
  ]
    await oreki.send_file(event.chat_id, IMAGE, caption=OREKI, buttons=BUTTON)
