from pyrogram import filters
from pyrogram.errors import RPCError

from OrekiRobot import pgram
from OrekiRobot.utils.pluginhelpers import admins_only, get_text

Oreki_PYRO_Captedit = filters.command("captedit")


@pgram.on_message(Oreki_PYRO_Captedit & ~filters.bot & ~filters.private)
@pgram.on_edited_message(Oreki_PYRO_Captedit)
@admins_only
async def loltime(message):
    lol = await message.reply("Processing please wait")
    cap = get_text(message)
    if not message.reply_to_message:
        await lol.edit("reply to any message to edit caption")
    reply = message.reply_to_message
    try:
        await reply.copy(message.chat.id, caption=cap)
        await lol.delete()
    except RPCError as i:
        await lol.edit(i)
        return
