from OrekiRobot import(
BOT_NAME
BOT_USERNAME
OWNER_ID
OWNER_USERNAME
)

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as oreki

OWNER_PIC = "https://te.legra.ph/file/a3c11493fda2ae1e7b63a.jpg"


@oreki.on.message(pattern=("/owner"))
async def awake(event):
    OWNER = """
    **╒═══「• OWNER INFO • 」**

🖤 **ID:** {OWNER_ID}
🖤 **First Name:** 【🇮🇳】𝙏𝙝𝙚 𝙂𝙩𝙖𝙨𝙝
🖤 **Second Name:** None
🖤 **Username:** {OWNER_USERNAME}
🖤 **Github:** [Awesome-Gtash](https://Github.com/Awesome-Gtash)
🖤 **Instagram:** [Awesome_Gtash](https://Instagram.com/Awesome_Gtash)
🖤 **YouTube:** [Gtash Universe](https://YouTube.com/@Gtash_Universe)

🎗 **SUPPORT:** [Gtash Association](https://telegram.dog/Gtash_Association)
🎗 **UPDATES:** [Gtash Updates](https://telegram.dog/Gtash_Updates)
"""

await oreki.send_file(event.chat_id, OWNER_PIC, caption=OWNER)

__mod_name__: Owner

BOT_PIC = "https://te.legra.ph/file/cf81f114b4e7f6bbf269e.jpg"

@oreki.on.message(pattern=("/bot"))
async def awake(event):
    BOT = """
    **╒═══「• BOT INFO • 」**

🖤 **First Name:** {BOT_NAME}
🖤 **Second Name:** None
🖤 **Username:** {BOT_USERNAME}
🖤 **Github:** [OrekiRobot-3](https://Github.com/Awesome-Gtash/OrekiRobot-3.git)

🎗 **SUPPORT:** [Gtash Association](https://telegram.dog/Gtash_Association)
🎗 **UPDATES:** [Gtash Updates](https://telegram.dog/Gtash_Updates)
"""

await oreki.send_file(event.chat_id, BOT_PIC, caption=BOT)

__mod_name__: Bot
