from telethon import Button

from OrekiRobot import tbot as tbot
from OrekiRobot.events import register

PHOTO = "https://te.legra.ph/file/3fad527f4557d914834ee.jpg"


@register(pattern=("/repo"))
async def awake(event):
    OREKI = """
         Hey Guys Prince Oreki's All Repos are Public Now 🎗️.
➖➖➖➖➖➖➖➖➖➖➖➖➖
Click The Repo 1,2,3 Buttons To get the Repo..🤞
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰 Thanks for your love & support❤️ 
It's Fully stable Repo so you can deploy & make your own Bot.
➖➖➖➖➖➖➖➖➖➖➖➖➖
Support: @Tiger_SupportChat
"""

    BUTTON = [
        [
            Button.url(
                "[► Repo 1 ◄]", "https://github.com/Awesome-Gtash/OrekiRobot-1.git"
            ),
            Button.url(
                "[► Repo 2 ◄]", "https://github.com/Awesome-Gtash/OrekiRobot-2.git"
        ),
    ],
    [
            Button.url(
                "[► Repo 3 ◄]", "https://github.com/Awesome-Gtash/OrekiRobot-3.git"
         ),
     ],
  ]
    await tbot.send_file(event.chat_id, PHOTO, caption=OREKI, buttons=BUTTON)
