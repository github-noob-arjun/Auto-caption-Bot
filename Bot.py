import os
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
from Config import API_ID, API_HASH, BOT_TOKEN, AUTH_CHANNEL

App = Client(
      "AutoCaptionBot",
      bot_token=BOT_TOKEN,
      api_id=API_ID,
      api_hash=API_HASH,
)

@App.on_message(filters.private & filters.command("start"))
async def start(client, update):
    text = f"""✅ Hey I'm Alive"""
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
  )


@App.on_message(filters.media & filters.chat(AUTH_CHANNEL)) #filters.channel)
async def caption(client, message: Message):
    k, _ = get_file_id(message)
    C = k.file_caption
    await message.edit(f"**__{C}__**",
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
