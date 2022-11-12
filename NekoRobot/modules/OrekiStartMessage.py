from pyrogram import __version__ as pyrover
from telegram import __version__ as ptb
from telethon import button
from telethon import __version__ as tlhver
from NekoRobot import tbot as tbot

START_PIC = ""

OREKI = """
Prince Oreki 왕자 Is Started!

➪ Uptime:</b> <code>{}</code>
➪ Python:</b> <code>{}</code>
➪ Pyrogram Version: {pyrover}
➪ Telethon Version: {tlhver}
➪ Python-Telegram-Bot Version: {ptb}
"""

BUTTON = [
    [
        Button.url("Help 🎗️", "https//t.me/OrekiXProRobot?start=help"),
    ]
]
await tbot.send file(-1001878260997, START_PIC, caption=OREKI, buttons=BUTTON)
