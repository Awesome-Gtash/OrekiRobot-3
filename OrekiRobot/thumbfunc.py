from pyrogram import filters
from OrekiRobot import ND
from OrekiRobot.database import find, delthumb, addthumb

@ND.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
    thumb = find(int(message.chat.id))[0]
    if thumb:
       await ND.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("**You dont have any custom Thumbnail** ⚠️") 
		
@ND.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
    delthumb(int(message.chat.id))
    await message.reply_text("**Custom Thumbnail Deleted Successfully** 🚫")
	
@ND.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id , file_id)
    await message.reply_text("**Your Custom Thumbnail Saved Successfully** ✅")
