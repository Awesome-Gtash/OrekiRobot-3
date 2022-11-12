from pyrogram import __version__ as pyrover
from telethon import __version__ as tlhver
from telegram import __version__ as ptb
from telethon import Button

START_PIC = "https://te.legra.ph/file/af9b448b3f64853a806d7.jpg"

OREKI = """
Prince Oreki 왕자 Is Started!

➪ Uptime:</b> <code>{}</code>
➪ Python Vesion:</b> <code>{}</code>
➪ Pyrogram Version: {pyrover}
➪ Telethon Version: {tlhver}
➪ Python-Telegram-Bot Version: {ptb}
"""
BUTTON = [
        [
            Button.url("  Help 🎗️", "https://t.me/OrekiXProRobot?start=help"),
        ]
    ]
    tbot.send_file(-1001878260997, START_PIC, caption=OREKI, buttons=BUTTON)
