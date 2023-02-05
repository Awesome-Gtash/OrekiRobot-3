from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import Button

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as bot

POSTER = ""

@bot(pattern=("Thunivu"))
async def awake(e):
    CAP = """
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

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600 
    seconds %= 3600 
    minutes = seconds // 60 
    seconds %= 60 
    return "%d:%02d:%02d" % (hour, minutes, seconds)

file1 = ""

async def awake(e):
    FILE_CAP = """
**Thunivu (2023) on HDRip 320p - x264 - Tamil - 250MB**
"""
 await oreki.send_file(event.chat_id, file1, caption=FILE_CAP)

file2 = ""

async def awake(e):
    FILE2_CAP = """
**Thunivu (2023) on HDRip 480p - x264 - Tamil - 400MB**
"""
 await oreki.send_file(event.chat_id, file2, caption=FILE2_CAP)

file3 = ""

async def awake(e):
    FILE3_CAP = """
**Thunivu (2023) on HDRip 720p - x264 - Tamil - 700MB**
"""
 await oreki.send_file(event.chat_id, file3, caption=FILE3_CAP)

file4 = ""

async def awake(e):
    FILE4_CAP = """
**Thunivu (2023) on HDRip 1080p - x264 - Tamil - 1.5GB**
"""
 await oreki.send_file(event.chat_id, file4, caption=FILE4_CAP)

async def awake(e):
 await event.reply("Processing Please wait!")
