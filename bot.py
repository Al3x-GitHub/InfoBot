import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Info Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """<b>Hello {}

I'm A Simple Telegram Info Gathering Bot, Click /help To Know My Commands And My Uses<b>"""

HELP_TEXT = """ğ¤ How To Use Me?

â¢ Forward a Message for take it's Details (in Private)
â¢ Send any Media to take its Details (in private)
â¢ Reply /info to a Message to take Message Details
â¢ Use /info Command to take your Details
â¢ Use /id in Group or Channel to get Unique Telegram ID"""

ABOUT_TEXT = """--**About Me**--

- **Bot :** `Info Bot`
- **Creator :** [IğÏÉ±i åæ³](https://telegram.me/MaximXRobot)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/Al3x-Github/InfoBot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="Developer", url=f"https://t.me/MaximXRobot")]])


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    
    text = f"""--**Information**--

**ğğ»ââï¸ First Name :** {update.from_user.first_name}
**ğ§ââï¸ Second Name :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**ğ§ğ»âğ Username :** {update.from_user.username}
**ğ Telegram ID :** {update.from_user.id}
**ğ Profile Link :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    await update.reply_text(        
        text=f"**Your Telegram ID :** {update.from_user.id}",
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


print("Bot Started! Now Join on @MaximXChannels")
Bot.run()
