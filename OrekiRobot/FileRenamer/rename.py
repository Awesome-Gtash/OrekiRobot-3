import humanize
import time
import os

from PIL import Image
from OrekiRobot.helper import progress_for_pyrogram, convert
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from OrekiRobot import ND, PREFIX
from pyrogram import filters
from OrekiRobot.database import find, insert
from pyrogram.types import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton



@ND.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename(_, message):
    insert(int(message.chat.id))
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id

    text = f"**Name**: `{filename}`\n\n"
    text += f"**File ID**: `{fileid}`\n\n"
    text += f"**File size**: `{filesize}`\n\n"
    text += f"**Choose the Button below to Rename it!**"
    
    button = InlineKeyboardMarkup([[
             InlineKeyboardButton(" Rename ✅", callback_data="rename"), 
             ],[ InlineKeyboardButton("Cancel 🚫", callback_data="cancel"),]])
    try:
      await message.reply_text(text=text, reply_markup=button, reply_to_message_id=message.id)
    except Expection:
         return await message.reply_text(Expection)


@ND.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
           await update.message.delete()
	except:
           return


@ND.on_callback_query(filters.regex("rename"))
async def cb_rename(_, query):
     await query.message.delete()
     await query.message.reply_text("🗒️ Enter File name",
        reply_to_message_id=query.message.reply_to_message.id, reply_markup=ForceReply(True))


@ND.on_message(filters.private & filters.reply)
async def refund(_, message):
     reply = message.reply_to_message
     if (reply.reply_markup) and isinstance(reply.reply_markup, ForceReply):

        new_name = message.text
        await message.delete()
        
        msg = await ND.get_messages(message.chat.id, reply.id)
        file = msg.reply_to_message
        media = file.media
        await reply.delete()

        button = [[InlineKeyboardButton("📁 File",callback_data = "upload:document")]]
        if str(media) in ["MessageMediaType.VIDEO", "MessageMediaType.DOCUMENT"]:
             button.append([InlineKeyboardButton("🎥 Video",callback_data = "upload:video")])
        elif str(media) == "MessageMediaType.AUDIO":
             button.append([InlineKeyboardButton("🎵 Audio",callback_data = "upload:audio")])
        await message.reply_text(
           f"**Select the output file type**\n**Output FileName**:- {new_name}",
           reply_to_message_id=file.id,
           reply_markup=InlineKeyboardMarkup(button))


@ND.on_callback_query(filters.regex("upload"))
async def doc(bot,query):
     type = query.data.split(":")[1].casefold()
     new_name = query.message.text
     new_filename = new_name.split(":-")[1].strip()
     if not "." in new_filename:
         if type == "document":
             new_filename = new_filename + ".mkv" 
         elif type == "audio":
             new_filename = new_filename + ".mp3"  
         elif type == "video":
             new_filename = new_filename + ".mp4" 
         else:
             new_filename = new_filename + ".mkv" 
     else:
         new_filename = new_filename

     file_path = f"downloads/{new_filename}"
     file = query.message.reply_to_message
     ms = await query.message.edit("Downloading...⚠️")
     c_time = time.time()
     try:
     	path = await ND.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳....",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return 
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
     except:
        pass
     user_id = int(query.message.chat.id) 
     ph_path = None
     data = find(user_id) 
     media = getattr(file, file.media.value)
     c_caption = data[1] 
     c_thumb = data[0]
     if c_caption:
         caption = c_caption.format(filename=new_filename, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
     else:
         caption = f"**{new_filename}**"
     if (media.thumbs or c_thumb):
         if c_thumb:
            ph_path = await ND.download_media(c_thumb) 
         else:
            ph_path = await ND.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")
     await ms.edit("Uploading....")
     c_time = time.time() 
     try:
        if type == "document":
           await ND.send_document(
		    query.message.chat.id,
                    document=file_path,
                    thumb=ph_path, 
                    caption=caption, 
                    progress=progress_for_pyrogram,
                    progress_args=( "Uploading....⚡",  ms, c_time   ))
        elif type == "video": 
            await ND.send_video(
		    query.message.chat.id,
		    video=file_path,
		    caption=caption,
		    thumb=ph_path,
		    duration=duration,
		    progress=progress_for_pyrogram,
		    progress_args=( "Uploading....⚡",  ms, c_time))
        elif type == "audio": 
            await ND.send_audio(
		    query.message.chat.id,
		    audio=file_path,
		    caption=caption,
		    thumb=ph_path,
		    duration=duration,
		    progress=progress_for_pyrogram,
		    progress_args=( "Uploading....⚡",  ms, c_time   )) 
     except Exception as e: 
         await ms.edit(e) 
         os.remove(file_path)
         if ph_path:
           os.remove(ph_path)
     await ms.delete() 
     os.remove(file_path) 
     if ph_path:
        os.remove(ph_path)
