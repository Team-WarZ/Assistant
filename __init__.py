# LEGENDBOT Assistant
from . import *
from telethon import Button, custom

from userbot import bot

from userbot import ALIVE_NAME
OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


LEGEND_USER = bot.me.first_name
Its_LegendBoy = bot.uid

legend_mention = f"[{LEGEND_USER}](tg://user?id={Its_LegendBoy})"
LEGEND_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
LEGEND_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
LEGEND_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
LEGEND_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
LEGEND_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
LEGENDversion = "𝚅2.1"

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
