from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import OWNER_ID
from m8n.config import ASSUSERNAME
from m8n.config import UPDATE
from m8n.config import SUPPORT
from m8n.config import OWNER_USERNAME
from m8n.config import BOT_NAME


@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Hello [πΊπ»ππ»]({START_PIC}) My name is **{BOT_NAME}**

I'm most complete voice chat music player for playing high quality and unbreakable music in your groups voice chat with some useful features.

Use inline buttons given below to know more about me !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Main Info π", callback_data="cbabout"),
                    InlineKeyboardButton(
                        "π Commands π", callback_data="cbevery")
       
                ],
                [
                    InlineKeyboardButton(
                        "π Others π", callback_data="others")
                ],
                [
                    InlineKeyboardButton(
                        "πβ Add Bot in Your Group βπ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds_set(_, query: CallbackQuery):
        await query.answer("commands menu")
        await query.edit_message_text(
        f"""Hello π [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 

Check out all the commands given below by Click on the given inline buttons !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π€Sudo Usersπ€", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("π€Everyoneπ€", callback_data="cbevery"),
                    InlineKeyboardButton("π€Group Adminsπ€", callback_data="cbadmins"),
                ],[
                    InlineKeyboardButton("β€οΈβπ©Ή Go Back β€οΈβπ©Ή", callback_data="cbhome")
                ],
            ]
        ),
    ) 


# Commands for Everyone !!
@Client.on_callback_query(filters.regex("cbevery"))
async def all_set(_, query: CallbackQuery):
    await query.answer("Everyone menu")
    await query.edit_message_text(
    f"""β’ /play (song name) or (YT link)
- plays the song in voice chat of your group 

β’ /song (song name) or (YT link)
- Downloads song in audio File 

β’ /tgm or /telegraph
- generate the link of given media

β’ /info 
- show all the information about a given user

β’ /search or /yt
- search link of the given song

β’ /ping
- Shows the ping message

β’ @botusername <query> 
- Get youtube url by inline mode""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton(
                        "πAdminsπ", callback_data="cbadmins"),
                    InlineKeyboardButton(
                        "πSudo/Ownerπ", callback_data="cbsudo")
                ],
              [InlineKeyboardButton("β€οΈβπ©Ή Go Back β€οΈβπ©Ή", callback_data="cbhome")]]
        ),
    )


# Commands for SudoUsers
@Client.on_callback_query(filters.regex("cbsudo"))
async def sudo_set(_, query: CallbackQuery):
    await query.answer("sudo menu")
    await query.edit_message_text(
    f"""β’ /restart 
- restarts the bot in Heroku 

β’ /gcast 
- broadcast your message with pin in the served Chats

β’ /broadcast 
- broadcast your message without pin in the served chats

β’ /exec <code> 
- Execute any Code given by a sudo user of the bot

β’ /stats
- shows the Bot's system stats

β’ /userbotleaveall
- force the music assistant of the bot to leave all the served Chats""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("β€οΈβπ©Ή Go Back β€οΈβπ©Ή", callback_data="cbevery")
                ],
            ]
        ),
    )


# Commands for Group Admins
@Client.on_callback_query(filters.regex("cbadmins"))
async def admin_set(_, query: CallbackQuery):
    await query.answer("admins menu")
    await query.edit_message_text(
    f"""β’ /skip 
- skips music in the voice Chat 

β’ /pause 
- Pause music in the voice chat 

β’ /resume 
- Resumes music in the voice Chat

β’ /end or /stop
- stop playing music in the group's voice chat

β’ /cleandb
- Clears all raw files in your group which is uploaded by bot

β’ /userbotjoin
- invites the music assistant of the bot in your group

β’ /userbotleave
- Bot's music assistant will leaves your group""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("β€οΈβπ©ΉGo Backβ€οΈβπ©Ή", callback_data="cbevery")
                ],
            ]
        ),
    )


# Bot about & Information
@Client.on_callback_query(filters.regex("cbabout"))
async def about_set(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""Hello π [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Click on the given inline buttons to know all the information about the Bot !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π§‘ Support π", url=f"https://t.me/{SUPPORT}"),
                    InlineKeyboardButton("π§‘ Updates π", url=f"https://t.me/{UPDATE}")
                ],[
                    InlineKeyboardButton("π Owner π", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("β£οΈ Assistant β£οΈ", url=f"https://t.me/{ASSUSERNAME}")
                ],[
                    InlineKeyboardButton("π Source Code π", url=f"https://t.me/bad_pipul")
                ],[
                    InlineKeyboardButton("β€οΈβπ©Ή Back β€οΈβπ©Ή", callback_data="cbhome")
                ],
            ]
        ),
    )


# OTHERS CALLBACK
@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Powered By : @{UPDATE}

After you played your song some menu buttons will be comes to manage your music playing on voice chat. All the buttons are as follows :

β’ βΈ 
- Resume Music
β’ βΆοΈ
- Pause Music
β’ βΉ 
- End Music
β’ β©
- Skip Music

Only admins can use this buttonsπ""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton("π§‘ Support π", url=f"https://t.me/{SUPPORT}"),
                    InlineKeyboardButton("π§‘ Updates π", url=f"https://t.me/{UPDATE}")
                ],
            [InlineKeyboardButton("Basic Guide & Full Set-up", callback_data="setup")],
            [InlineKeyboardButton("β€οΈβπ©Ή Back Home β€οΈβπ©Ή", callback_data="cbhome")]]
        ),
    )

@Client.on_callback_query(filters.regex("setup"))
async def setup(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Basic SetUp Guide for the Bot Usage :**


β’ Add this Bot in your Group.

β’ Promote it as an administrator with needed powers.

β’ Now send /play or /userbotjoin command to invite assistant id in your Chat.

β’ Your All the Set-Up is Done, Now enjoy your favourite music in your groups voice chat without any limitations.


Thanks !!
Please don't forget to Join our Group :
@{UPDATE}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("β€οΈβπ©Ή Go Back β€οΈβπ©Ή", callback_data="others")
                ],
            ]
        ),
    )
