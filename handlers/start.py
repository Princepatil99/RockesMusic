from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BOT_NAME, BOT_USERNAME, GROUP_SUPPORT, OWNER_NAME, UPDATES_CHANNEL
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.mention} !** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Mujhey Use Ker Key Ap Koe Bhi Song Play Ker Sakty Hain Ap Bas Apneh Group Main Add Kro Aur Admin Bana Do Developer @Dr_Asad_AlI $ This allows you to play music on groups through the new Telegram's voice chats!**

💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**

❔ **To know how to use this bot, please click on the » ❓ Basic Guide button!**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ 𝗕𝗮𝘀𝗶𝗰 𝗚𝘂𝗶𝗱𝗲", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 🅒︎𝐨𝐦𝐦𝐚𝐧𝐝🅢︎", callback_data="cbcmds"),
                    InlineKeyboardButton("💝 🅟𝐫𝐢𝐞𝐧𝐜🅔︎", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 🅖︎𝐫𝐨𝐮🅟︎", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 🅒𝐡𝐚𝐧𝐧𝐞🅛︎", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 🅚𝐢𝐧🅖︎", url="https://www.youtube.com/jankarikiduniya"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    
    keyboard=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ 🅖︎𝐫𝐨𝐮🅟︎", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 🅒︎𝐡𝐚𝐧𝐧𝐞🅛︎", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ]
            ]
        )
    
    alive = f"✨ 𝐁𝐨𝐭 𝐈𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 🤗...\n\n✨ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐈𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠...\n\n✨ 𝗨𝗽𝘁𝗶𝗺𝗲 𝗦𝘁𝗮𝘁𝘂𝘀: `{uptime}`"
    
    await message.reply_photo(
        photo="https://telegra.ph/file/dbfb37d283ae466692ada.jpg",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="❔ HOW TO USE ME", callback_data="cbguide")]]
        ),
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 Advanced Cmd", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Sudo Cmd", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 Owner Cmd", callback_data="cbowner")],
                [InlineKeyboardButton("📔 Fun Cmd", callback_data="cbfun")],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
