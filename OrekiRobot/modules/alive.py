"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022-2023, Awesome-Gtash, [ https://github.com/Awesome-Gtash]
Copyright (c) 2022-2023, White Tiger • Network, [ https://github.com/Awesome-Gtash/OrekiRobot-3 ]
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import asyncio
import datetime
from datetime import datetime

from pyrogram import __version__ as pyrover
from telethon import Button
from telethon import __version__ as tlhver

from OrekiRobot import BOT_NAME
from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

edit_time = 5
""" =======================Oreki====================== """
file1 = "https://te.legra.ph/file/e3a37df24dd0965dba2cf.jpg"
file2 = "https://te.legra.ph/file/0de0f032e682c031f17d9.jpg"
file3 = "https://te.legra.ph/file/283d0016973127a7f6cbf.jpg"
file4 = "https://te.legra.ph/file/964030fa52d6dcc53fe4d.jpg"
file5 = "https://te.legra.ph/file/d64efaf679941b87b1341.jpg"
""" =======================Oreko====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Oreki = f"** ♡ Hola I'm {BOT_NAME}!**\n\n"
    Oreki += f"**♡ My Uptime ~ 🖤:** `{uptime}`\n\n"
    Oreki += f"**♡ Python-telegram-bot Version ~ 🖤 :** `{ptb}`\n\n"
    Oreki += f"**♡ Telethon Version ~ 🖤:** `{tlhver}`\n\n"
    Oreki += f"**♡ Pyrogram Version ~ 🖤:** `{pyrover}`\n\n"
    Oreki += "**♡ My Master ~ 🖤 :** [Myaav Boi](https://t.me/Awesome_MB) "
    BUTTON = [
        [
            Button.url("【► Updates ◄】", f"https://t.me/Tiger_Updates"),
            Button.url("【► Support ◄】", f"https://t.me/Tiger_SupportChat"),
        ]
    ]
    on = await oreki.send_file(yes.chat_id, file=file2, caption=Oreki, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await oreki.edit_message(yes.chat_id, on, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok2 = await oreki.edit_message(yes.chat_id, ok, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await oreki.edit_message(yes.chat_id, ok2, file=file1, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok4 = await oreki.edit_message(yes.chat_id, ok3, file=file2, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await oreki.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok6 = await oreki.edit_message(yes.chat_id, ok5, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok7 = await oreki.edit_message(yes.chat_id, ok6, file=file4, buttons=BUTTON)
