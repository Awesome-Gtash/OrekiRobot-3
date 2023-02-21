# Oreki Example Plugin Format

## Advanced: Decorators
```python3

from OrekiRobot.modules.helper_funcs.decorators import orekicmd
from telegram import Update
from telegram.ext import CallbackContext

@orekicmd(command='oreki', pass_args=True)
def oreki(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text("oreki")

    
__mod_name__ = "Oreki"
__help__ = """
<b>Oreki</b>
- /oreki: ......
"""
```



## Advanced: Pyrogram
```python3
from OrekiRobot import pgram

Oreki_PYRO_Hello = filters.command("oreki")

@pgram.on_message(Oreki_PYRO_Hello) & ~filters.edited & ~filters.bot)
async def hmm(client, message):
    j = "Hello I'm oreki"
    await message.reply(j)
   
__mod_name__ = "Oreki"
__help__ = """
<b>Oreki</b>
- /oreki: ......
"""
```

## Advanced: Telethon
```python3

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as oreki

@oreki(pattern="^/oreki")
async def hmm(event):
    j = "Hello I'm oreki"
    await event.reply(j)
    
__mod_name__ = "Oreki"
__help__ = """
<b>Oreki</b>
- /oreki: ......
"""
```

## Advanced: MOD
```python3

from OrekiRobot import OREKI_MOD
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def oreki(update: Update, context: CallbackContext):
    j = "hello"
    update.effective_message.reply_text(j)

HANDLER = CommandHandler("oreki", oreki, run_async=True)
OREKI_MOD.add_handler(HANDLER)

__handlers__ = [ HANDLER, ]
    
__mod_name__ = "Oreki"
__help__ = """
<b>Oreki</b>
- /oreki: ......
"""
```
