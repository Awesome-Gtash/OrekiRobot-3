from telethon import Button

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

PHOTO = "https://te.legra.ph/file/4406fa4db464bf8316c7f.jpg"

@register(pattern=("Hi"))
async def awake(event):
    NEKO = f"{event.sender.first_name} Hello Friend How are you?!"
    BUTTON = [
        [
            Button.url(" Updates 🔮", "https://telegram.dog/Updates004"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)

__help__ = """
/hi: It will Reply as hi.
"""

__mod_name__ = "Hi"
__command_list__ = ["Hi/Hello"]
