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
            Button.url(
                "[► Repo 1 ◄]", "https://github.com/Awesome-Gtash/OrekiRobot-1.git"
         ),
     ],
  ]
    await oreki.send_file(event.chat_id, PHOTO, caption=OREKI, buttons=BUTTON)
