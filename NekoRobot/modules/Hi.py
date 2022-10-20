from telethon import Button

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/84696d6e1bebe28976e5a.jpg"
file2 = "https://te.legra.ph/file/f30b3e091288e185414a3.jpg"
file3 = "https://te.legra.ph/file/4624003c955098d4a4613.jpg"
file4 = "https://te.legra.ph/file/f5856e243e9c03d1ed501.jpg"
file5 = "https://te.legra.ph/file/4406fa4db464bf8316c7f.jpg"
""" =======================CONSTANTS====================== """


@register(pattern="/hi")

@register(pattern=("Hello"))
async def awake(event):
    NEKO = f"{event.sender.first_name} Hello Friend How are you?!"
    BUTTON = [
        [
            Button.url(" Updates 🔮", "https://telegram.dog/Updates004"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
    
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

__help__ = """
/hi: shows your info in inline button
"""

__mod_name__ = "Hi"
__command_list__ = ["Hi"]
