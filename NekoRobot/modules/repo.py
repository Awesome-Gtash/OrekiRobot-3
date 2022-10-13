"""
MIT License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022 Awesome-Prince
Copyright (c) 2022, Koyūki • Network, <https://github.com/Awesome-Prince/NekoRobot-3>
This file is part of @NekoXRobot (Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the Software), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from telethon import Button

from NekoRobot import tbot as tbot
from NekoRobot.events import register

PHOTO = "https://telegra.ph/file/ab9f474736175a18f1a83.jpg"


@register(pattern=("/repo"))
async def awake(event):
    NEKO = """
         We Are So Happy To Announce That We Have Public Our OrekiRobot Repo. ✨🥀
➖➖➖➖➖➖➖➖➖➖➖➖➖
「@OrekiXPro_bot」
➖➖➖➖➖➖➖➖➖➖➖➖➖
Here is the Repo Deploy your Own OrekiRobot.
⚜️Repo ➤ https://github.com/Awesome-Gtash/OrekiRobot.git
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰 Thanks for your support 
It's Fully stable Repo so you can deploy and make own Bot.
──────────────────
Powered By:- @Tiger_Networkk
"""

    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
