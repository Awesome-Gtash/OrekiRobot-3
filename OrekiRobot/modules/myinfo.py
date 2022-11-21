import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from OrekiRobot import tbot as bot
from OrekiRobot import tbot as tgbot
from OrekiRobot.events import register

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/89b904cc6929e3018f31e.jpg"
file2 = "https://te.legra.ph/file/ef94e5c2acb389edef9a9.jpg"
file3 = "https://te.legra.ph/file/0433e4802b235a8e55b8f.jpg"
file4 = "https://te.legra.ph/file/27a10045aae7e46534436.jpg"
file5 = "https://te.legra.ph/file/197d0508537753ea61850.jpg"
""" =======================CONSTANTS====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("Your Info", data="information")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"♡ Hey {betsy}, I'm Oreki\n♡ I'm Created By [Myaav Boi](tg://user?id=5189767566)\n♡ Click The Button Below To Get Your Info",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        OREKI = "YOUR DETAILS BY OREKI  \n\n"
        OREKI += f"FIRST NAME : {PRO.first_name} \n"
        OREKI += f"LAST NAME : {PRO.last_name}\n"
        OREKI += f"YOU BOT? : {PRO.bot} \n"
        OREKI += f"RESTRICTED USER? : {PRO.restricted} \n"
        OREKI += f"USER ID : {boy}\n"
        OREKI += f"USERNAME : {PRO.username}\n"
        await event.answer(OREKI, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__help__ = """
/myinfo: shows your info in inline button
"""

__mod_name__ = "Myinfo"
__command_list__ = ["Myinfo"]
