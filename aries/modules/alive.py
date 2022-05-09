from telethon import Button

from aries import telethn as tbot
from aries.events import register

PHOTO = "https://telegra.ph/file/c1dc3b841a5ced3cdbe4b.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
    event.sender.first_name
    ARIES = "**Hello i'm Akira** \n\n"
    ARIES += "**All System are Working Properly**\n"
    ARIES += " ☬ ⌊ **Python :** __3.9.7__ ⌉\n"
    ARIES += " ☬ ⌊ **Pyrogram :** __1.2.9__ ⌉\n"
    ARIES += " ☬ ⌊ **MongoDB :** __2.5.1__ ⌉\n"
    ARIES += " ☬ ⌊ **Platform :** __linux__ ⌉\n"
    ARIES += " ☬ ⌊ **My Lord** : [너를 •](https://t.me/DreamereNo1) ☠⌉\n"
    ARIES += " ☬ ⌊ **αҡเ૨α รɦเ૨σყαɳαɠเ** ⌉\n\n"
    ARIES += " ☬ ⌊ **Telethon : 6.6.6 Latest** ⌉\n\n"
    ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
    BUTTON = [
        [
            Button.url("Support", "https://t.me/NovusSupport"),
            Button.url("Owner", "https://t.me/DreamerNo1"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=ARIES, buttons=BUTTON)


__mod_name__ = "Alive"
