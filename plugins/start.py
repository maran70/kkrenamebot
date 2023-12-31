from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from helper.txt import mr
from helper.database import insert 
from helper.utils import not_subscribed 

START_PIC = environ.get("START_PIC", "https://i.ibb.co/0C292SX/8de305e8631dbd22facbd0a14622490f.jpg")

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink) ]]
    text = "**𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴 𝚈𝙾𝚄𝚁 𝙽𝙾𝚃 𝙹𝙾𝙸𝙽𝙳 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 😔. 𝙿𝙻𝙴𝙰𝚂𝙴 𝙹𝙾𝙸𝙽 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 🙏**\n\ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/BotCreator99>@BotCreator99</a>"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""👋 𝗛𝗶𝗶 {message.from_user.mention} \n𝗜'𝗺 𝗔 𝗦𝗶𝗺𝗽𝗹𝗲 𝗙𝗶𝗹𝗲 𝗥𝗲𝗻𝗮𝗺𝗲+𝗙𝗶𝗹𝗹𝗲 𝗧𝗼 𝗩𝗶𝗱𝗲𝗼 𝗖𝗼𝘃𝗲𝗿𝘁𝗲𝗿 𝗕𝗼𝘁 𝗪𝗶𝘁𝗵 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 & 𝗖𝘂𝘀𝘁𝗼𝗺 𝗖𝗮𝗽𝘁𝗶𝗼𝗻 𝗦𝘂𝗽𝗽𝗼𝗿𝘁!\nℹ️ 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/BotCreator99>@BotCreator99</a> """,
       reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/BotMinister'),
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿', callback_data='help')
                 ]]
                )
            )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`""",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 𝚁𝙴𝙽𝙰𝙼𝙴 𝙽𝙾𝚆 📝",callback_data = "rename")],
        [InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 Hai {query.from_user.mention} \n I am a super renamer bot! 😄""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton('❤️ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/BotMinister'),
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿', callback_data='help')
                 ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🤔🤔 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴  🤔🤔", url='https://t.me/BotMinister')
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





