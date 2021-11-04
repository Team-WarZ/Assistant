from telethon import events
from . import *
from userbot import ALIVE_NAME
from userbot import bot

LEGEND_USER = bot.me.first_name
Its_LegendBoy = bot.uid
legend_mention = f"[{LEGEND_USER}](tg://user?id={Its_LegendBoy})"

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"


PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『Lêɠêɳ̃dẞø†』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{legend_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『Lêɠêɳ̃dẞø†』~ `{LEGENDversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Its_LegendBot)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/LEGEND-OS/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Lêɠêɳ̃dẞø†』 ](https://t.me/Legend_Userbot)\n"
pm_caption += f"┣Assistant ~ By [『Lêɠêɳ̃dẞøy』 ](https://t.me/Its_LegendBoy)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『Lêɠêɳ̃dẞø†』](https://t.me/Legend_Userbot) «««"


# only Owner Can Use it

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
