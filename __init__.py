from . import *
from telethon import Button, custom

from userbot import bot

from userbot import ALIVE_NAME
OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


LEGEND_USER = bot.me.first_name
Its_LegendBoy = bot.uid

legend_mention = f"[{LEGEND_USER}](tg://user?id={Its_LegendBoy})"

perf = "[ †hê Lêɠêɳ̃dẞø† ]"


DEVLIST = [
    "2082798662"
]

async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
