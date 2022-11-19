from pyrogram import Client, filters
from pyrogram.types import Message

from OrekiRobot import OWNER_ID
from OrekiRobot import pgram as bot


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if message.from_user.id != 5189767566:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
