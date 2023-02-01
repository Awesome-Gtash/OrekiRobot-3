# this module made by me this is my own module
# thanks for my friend he gave me some ideas @Otazuki_004

from telethon import Button
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from OrekiRobot import BOT_NAME
from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

IMAGE = "https://te.legra.ph/file/191a2b533e49ddd8f63cc.jpg"

@register(pattern=("Varisu"))
async def awake(event):
      IMG_CAPTION = """
*Results for Varisu*
"""

BUTTON = [
     [
       InlineKeyboardButton(
       text=f"Download [285.9MB] File", callback data="file1"),
       text=f"Download [436.4MB] File", callback data="file2"),
       text=f"Download [711.1MB] File", callback data="file3"),
       text=f"Download [1.07GB] File", callback data="file4"),
       text=f"Download [1.74GB] File", callback data="file5"),
     ]
]
 await oreki.send_file(event.chat_id, IMAGE, caption=IMG_CAPTION, buttons=BUTTON)



file1 = "https://t.me/OrekiMovies/6"

FILE1_CAP = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
 await oreki.send_file(event.chat_id, file=file1, caption=FILE1_CAP)


file2 = "https://t.me/OrekiMovies/7"

FILE2_CAP = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
 await oreki.send_file(event.chat_id, file=file2, caption=FILE2_CAP)


file3 = "https://t.me/OrekiMovies/8"

FILE3_CAP = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
 await oreki.send_file(event.chat_id, file=file3, caption=FILE3_CAP)


file4 = "https://t.me/OrekiMovies/9"

FILE4_CAP = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
 await oreki.send_file(event.chat_id, file=file4, caption=FILE4_CAP)


file5 = "https://t.me/OrekiMovies/10"

FILE5_CAP = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
 await oreki.send_file(event.chat_id, file=file5, caption=FILE5_CAP)



@register(pattern=("Varisu"))
async def awake(event):
  await event.reply("**➠ Uploaded by : {BOT_NAME}**")
