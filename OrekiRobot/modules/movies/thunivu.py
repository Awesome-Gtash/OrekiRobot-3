from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import Button

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as bot

POSTER = ""

@bot(pattern=("Thunivu"))
async def awake(e):
    CAP """
Choose the size of Thunivu
"""

FIRST_BUTTON = [
        [
               InlineKeyboardButton(
               text="[247.7MB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file1"
               text="[399.5MB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file2"
               text="[700.3MB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file3"
               text="[1.41GB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file4"
        ),
  )
 await oreki.send_file(event.chat_id, POSTER, caption=CAP, buttons=FIRST_BUTTON)

file1 = ""

async def awake(e):
    FILE_CAP = """
Thunivu () All Episodes 720p - x264 - Tamil - 250MB
