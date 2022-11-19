from telethon import Button

from OrekiRobot import tbot as tbot
from OrekiRobot.events import register

PHOTO = "https://te.legra.ph/file/51e5179533e2cd4527d31.jpg"


@register(pattern=("?Credits"))
async def awake(event):
    OREKI = """
    **Credits:-**

**MASTER :** [MYAAV BOI](t.me/Awesome_MB)
**DEV :** [LOVELY PRINCE](t.me/Awesome_Prince)
**HELPER :** [OTAZUKI](t.me/Otazuki_004)
**REPO LINK :** [CLICK HERE](https://github.com/Awesome-Gtash/OrekiRobot-3.git)
➖➖➖➖➖➖➖➖➖➖➖➖➖
**I Hope You All Guys!!!!**

**Become a Best Programmers List!. Thanking You!!!**
"""

    BUTTON = [
        [
            Button.url(" 📢 Updates  ", "https://telegram.dog/Tiger_Updates"),
            Button.url(" Support 🛡️ ", "https://telegram.dog/Tiger_SupportChat"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=OREKI, buttons=BUTTON)
