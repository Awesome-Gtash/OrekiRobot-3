from pyrogram import __version__ as pyrover
from telegram import __version__ as ptb
from telethon import Button
from telethon import __version__ as thlver

OREKI_PIC = "https://te.legra.ph/file/61bbf07e33a148006dc67.jpg"

START_OREKI = f"""
Prince Oreki 왕자 Is Started!

➪ Uptime:<b><code>{}<b><code>
➪ Python Version:<b><code>{}<b><code>
➪ Pyrogram Version: {pyrover}
➪ Telethon Version: {thlver}
➪ Python-Telegram-Bot Version: {ptb}
"""

START_BUTTON = [
    [
        Button.url("Help 🎗️", "https://t.me/orekixprorobot?start=help"),
    ]
]
await tbot.send_file(-1001878260997, OREKI_PIC, caption=OREKI, buttons=BUTTON),
