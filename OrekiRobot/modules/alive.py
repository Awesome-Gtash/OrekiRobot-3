from pyrogram import __version__ as pyrover
from telethon import Button
from telegram import __version__ as ptb
from telethon import __version__ as tlhver

from OrekiRobot import BOT_NAME
from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

IMAGE = "https://te.legra.ph/file/3fad527f4557d914834ee.jpg"


@register(pattern=("/alive"))
async def awake(event):
    OREKI = """
**Hola I'm {BOT_NAME}!**
**♡ My Uptime ~ 🖤:** `{uptime}`\n\n
**♡ Python-Telegram-Bot Version ~ 🖤 :** `{ptb}`\n\n
**♡ Telethon Version ~ 🖤:** `{tlhver}`\n\n
**♡ Pyrogram Version ~ 🖤:** `{pyrover}`\n\n
**♡ My Master ~ 🖤 :** [GTASH](https://t.me/Awesome_Gtashxd)
"""

    BUTTON = [
        [
            Button.url(
                "[► Repo 1 ◄]", "https://github.com/Awesome-Gtash/OrekiRobot-1.git"
            ),
            Button.url(
                "[► Repo 2 ◄]", "https://github.com/Awesome-Gtash/OrekiRobot-2.git"
        ),
    ],
    [
            Button.url(
                "[► Repo 3 ◄]", "https://github.com/Awesome-Gtash/OrekiRobot-3.git"
         ),
     ],
  ]
    await tbot.send_file(event.chat_id, PHOTO, caption=OREKI, buttons=BUTTON)
