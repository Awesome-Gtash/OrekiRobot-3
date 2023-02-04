from telethon import Button

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as bot

POSTER = ""

@bot(pattern("Thunivu"))
async def awake(event):
   CAPTION """
**Choose the File size Of Thunivu**
"""

F_BUTTON =  [
     (
         InlineKeyboardButton
            text="247.9MB File", url="file1",
            text="399.5MB File", url="file2",
            text="700.3MB File", url="file3",
            text="1.41GB File", url="file4",
        ),
    )
 await oreki.send_file(event.chat_id, POSTER, caption=CAPTION, buttons=F_BUTTON)

file1 = ""

async def awake(event):
   FILE_CAPTION """
**Thunivu (2023) HDRip on 320p - x264 - Tamil - 250MB**
"""
 await oreki.send_file(event.chat_id, File1, caption=FILE_CAPTION)


