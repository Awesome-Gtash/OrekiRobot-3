from telethon import Button



from OrekiRobot import tbot as oreki
from OrekiRobot.events import register as oreki

PHOTO = "https://te.legra.ph/file/a3c11493fda2ae1e7b63a.jpg"


@oreki.on.message(pattern=("/owner"))
async def awake(event):
    OREKI = """
    **╒═══「• OWNER INFO • 」**

🖤 **ID:** 5534661034
🖤 **First Name:** 【🇮🇳】𝙏𝙝𝙚 𝙂𝙩𝙖𝙨𝙝
🖤 **Second Name:** None
🖤 **Username:** @Awesome_Gtashxd
🖤 **Github:** [Awesome-Gtash](https://Github.com/Awesome-Gtash)
🖤 **Instagram:** [Awesome_Gtash](https://Instagram.com/Awesome_Gtash)
🖤 **YouTube:** [Gtash Universe](https://YouTube.com/@Gtash_Universe)

🎗 **SUPPORT:** [Gtash Association](https://telegram.dog/Gtash_Association)
🎗 **UPDATES:** [Gtash Updates](https://telegram.dog/Gtash_Updates)
"""
