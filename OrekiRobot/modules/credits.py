from telethon import Button

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

PHOTO = "https://te.legra.ph/file/013365b3d0b9e514ac388.jpg"


@register(pattern=("/credits"))
async def awake(event):
    OREKI = """
     **Credits:**

**Owner ~** [The Gtash](https://t.me/Awesome_Gtashxd)
**Co-owner ~** [OTAZUKI](https://t.me/Otazuki_004)

**SUPPORT:** [Gtash Association](https://t.me/Gtash_Association)
**UPDATES:** [Gtash Updates](https://t.me/Gtash_Updates)
"""

    BUTTON = [
        [
            Button.url("Gtash Association", "https://telegram.dog/Gtash_Association"),
            Button.url("Gtash Updates", "https://telegram.dog/Gtash_Updates"),
        ]
    ]
    await oreki.send_file(event.chat_id, PHOTO, caption=OREKI, buttons=BUTTON)
