from telethon import events, Button, custom
import re, os
from Flare-Robot.events import register
from Flare-Robot import telethn as tbot
from Flare-Robot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1cd6d62ef6e8843e6b1cb.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m ғʟᴀʀᴇ ʀᴏʙᴏᴛ 愛 ** \n\n"
  PIKACHU += "**♡ I'm Working With sᴇxʏ Speed**\n\n"
  PIKACHU += "**♡ ғʟᴀʀᴇ: LATEST Version**\n\n"
  PIKACHU += "**♡ My Creator: [ᴀsᴛᴀ](http://t.me/Chifuyu_Matsuno_Kun)\n\n"
  PIKACHU += "**♡ ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ @Freia_Support **\n"
  PIKACHU += "**♡ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 💘💘💘**\n"

  BUTTON = [[Button.url("🚑 Support", "https://t.me/Freia_Support"), Button.url("📢 Updates", "https://t.me/Freia_Updates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


__mod_name__ = "Alive"
