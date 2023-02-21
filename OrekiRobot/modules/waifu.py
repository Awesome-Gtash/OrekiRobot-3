import requests
from telegram import ParseMode

from OrekiRobot.events import register as oreki


@oreki(pattern="[/!]waifu")
async def ok(event):
    url = "https://api.waifu.pics/sfw/waifu"
    r = requests.get(url)
    e = r.json()
    await event.reply(
        "**A waifu appeared!** \nAdd them to your harem by sending /protecc character name",
        parse_mode=ParseMode.MARKDOWN,
        file=e["url"])


@oreki(pattern="[/!]protecc")
async def ok(event):
    await event.reply(
        "OwO you protecc'd A Waifu This waifu has been added to your harem.")


@oreki(pattern="[/!]harem")
async def ok(event):
    await event.reply("You haven't protecc'd any waifu yet...")
