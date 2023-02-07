from telethon import Button

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as bot

PHOTO = "https://te.legra.ph/file/3fad527f4557d914834ee.jpg"


@bot(pattern=("Oreki"))
async def awake(event):
    OREKI = """
Yes Iam Here
"""

    BUTTON = [
        [
            InlineKeyboardButton(text="🎗️ Help", callback_data="help_back"),
     ],
  ]
    await oreki.send_file(-1001585435524, PHOTO, caption=OREKI, buttons=BUTTON)
