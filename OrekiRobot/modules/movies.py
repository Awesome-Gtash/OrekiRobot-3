# this module created by me and my friend @Otazuki_004

from telethon import Button

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

POSTER = "https://t.me/OrekiMovies/7"

@register(pattern=("Thunivu"))
async def awake(event):
    CAP = """
THUNIVU

➤ Year : 2023
➤ Lang : Tamil
➤ Quality : HDRip
➤ Genre : Action, Thriller
➤ Size : 250MB-1.41GB

𖦹 Powered By : @Gtash_Association
"""

 await oreki.send_file(event.chat_id, POSTER, caption=CAP)

file1 = "https://t.me/OrekiMovies/8"

async def awake(event):
    FILE_CAP = """
**Thunivu (2023) on HDRip 320p - x264 - Tamil - 250MB**
"""
 await oreki.send_file(event.chat_id, file1, caption=FILE_CAP)

file2 = "https://t.me/OrekiMovies/9"

async def awake(event):
    FILE2_CAP = """
**Thunivu (2023) on HDRip 480p - x264 - Tamil - 400MB**
"""
 await oreki.send_file(event.chat_id, file2, caption=FILE2_CAP)

file3 = "https://t.me/OrekiMovies/10"

async def awake(event):
    FILE3_CAP = """
**Thunivu (2023) on HDRip 720p - x264 - Tamil - 700MB**
"""
 await oreki.send_file(event.chat_id, file3, caption=FILE3_CAP)

file4 = "https://t.me/OrekiMovies/11"

async def awake(event):
    FILE4_CAP = """
**Thunivu (2023) on HDRip 1080p - x264 - Tamil - 1.5GB**
"""
 await oreki.send_file(event.chat_id, file4, caption=FILE4_CAP)

async def awake(event):
 await send.message("➠ Uploaded by : @OrekiProXBot!")

__mod_name__ = "Thunivu"
