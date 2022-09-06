import os
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
from Config import API_ID, API_HASH, BOT_TOKEN, AUTH_CHANNEL, ANIME_CHANNEL, FILIM_GPY_CHANNEL, AUTOFILTER_CHANNEL

App = Client(
      "AutoCaptionBot",
      bot_token=BOT_TOKEN,
      api_id=API_ID,
      api_hash=API_HASH,
)

@App.on_message(filters.private & filters.command("start"))
async def start(client, update):
    text = """✅ Hey I'm Auto caption bot..!
I Can work only Some Channels.
"""
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True,
  )


@App.on_message(filters.media & filters.chat(AUTH_CHANNEL)) #filters.channel)
async def caption(client, message: Message):
    C = message.caption #get_file_id(message)
    await message.edit_caption(f"**__{C}__**\n\n**__Uploaded By : @MovieJunctionGrp__** 🔥",
          #reply_markup=InlineKeyboardMarkup(
             # [[
             # InlineKeyboardButton(f"{BUTTON_TEXT}", url=f"{URL_LINK}")
             # ]]
          )#)

@App.on_message(filters.media & filters.chat(ANIME_CHANNEL)) #filters.channel)
async def caption(client, message: Message):
    C = message.caption #get_file_id(message)
    await message.edit_caption(f"**__{C}__**\n**__━━━━━━━━━━━━━━━━━━━━━━\n➠ ɢʀᴏᴜᴘ ➧ @Moviejunction_Group\n➠ ᴄʜᴀɴɴᴇʟ ➧ @Mj_Linkz\n➠ ᴄʜᴀɴɴᴇʟ ➧ @Mj_Animations__**",
          #reply_markup=InlineKeyboardMarkup(
             # [[
             # InlineKeyboardButton(f"{BUTTON_TEXT}", url=f"{URL_LINK}")
             # ]]
          )#)

@App.on_message(filters.media & filters.chat(FILIM_GPY_CHANNEL)) #filters.channel)
async def caption(client, message: Message):
    C,_ = message.caption.split("Uploaded")
    #C = message.caption #get_file_id(message)
    await message.edit_caption(f"""**__{C}
━━━━━━━━━━━━━━━━━━━━━━
➠ ɢʀᴏᴜᴘ ➧ @Moviejunction_Group
➠ ᴄʜᴀɴɴᴇʟ ➧ @Mj_Linkz
➠ ᴄʜᴀɴɴᴇʟ ➧ @Mj_Filmography__**""",
          #reply_markup=InlineKeyboardMarkup(
             # [[
             # InlineKeyboardButton(f"{BUTTON_TEXT}", url=f"{URL_LINK}")
             # ]]
          )#)

@App.on_message(filters.media & filters.chat(AUTOFILTER_CHANNEL)) #filters.channel)
async def caption(client, message: Message):
    try:
        C,_ = message.caption.split("Uploaded")
    else:
        C = message.caption #get_file_id(message)
        await message.edit_caption(f"**__{C}__**",
              #reply_markup=InlineKeyboardMarkup(
                 # [[
                 # InlineKeyboardButton(f"{BUTTON_TEXT}", url=f"{URL_LINK}")
                 # ]]
              )#)

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id

App.run()
print("AutoCaptionBot Working Now..⚡⚡⚡")
