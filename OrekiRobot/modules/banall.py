from Meta import * 
from Meta.config import *
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["banallt"], prefixes=HANDLER))
async def banall_handler(_, m: Message):
    await m.delete()
    try: 
        count = 0
        data = []
        data.clear()
        async for x in app.get_chat_members(m.chat.id):
            if x.status == ChatMemberStatus.MEMBER:
                await app.ban_chat_member(m.chat.id, x.user.id)
                count += 1
    except Exception as e:
        await m.reply_text('**Aᴜɴᴛʏ Yᴏᴜ Aʀᴇ Nᴏᴛ Aɴ Aᴅᴍɪɴ -!**')
    await m.reply_text(f"**Bᴀɴɴᴇᴅ {count} ᴍᴇᴍʙᴇʀs -!**")
