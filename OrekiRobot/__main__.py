import contextlib
import html
import importlib
import json
import random
import re
import time
import traceback
from sys import argv

from pyrogram import __version__ as pyrover
from pyrogram import idle
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import escape_markdown
from telethon import Button
from telethon import __version__ as tlhver

import OrekiRobot.modules.sql.users_sql as sql
from OrekiRobot import (
    BOT_USERNAME,
    DONATION_LINK,
    HELP_IMG,
    LOGGER,
    OWNER_ID,
    OREKI_MOD,
    PORT,
    SUPPORT_CHAT,
    TOKEN,
    WEBHOOK,
    StartTime,
    pgram,
    tbot,
    updater,
)

# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from OrekiRobot.modules import ALL_MODULES
from OrekiRobot.modules.helper_funcs.chat_status import is_user_admin
from OrekiRobot.modules.helper_funcs.misc import paginate_modules


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


HELP_MSG = "Click The Button Below To Get Help Menu In Your Dm."
START_MSG = "I'm Awake Already!\n<b>Haven't Slept Since:</b> <code>{}</code>"

OREKI_STICKERS = (
    "CAACAgQAAx0CXn_ThAACDM5j9IyGH8BGp8qDTTnv35zHWvZJcgAC2AoAApkBwVDFFzmCmWTH7y4E",
    "CAACAgUAAx0CXn_ThAACDNBj9IyH_jaoK59cUYMfSJOrQy8KggAChAIAAkgNqFQDtDS2UaaygS4E",
    "CAACAgQAAx0CXn_ThAACDM9j9IyGcasAAZJEB4sl1hrfByhFa9EAAs0JAAKLoMFQuFgxj-VyyeIuBA",
    "CAACAgUAAx0CXn_ThAACDNFj9IyH1BFITPLEC794-ahvzROjVQAC7AEAAiKhqFScPNyYf5O8pi4E",
    "CAACAgQAAx0CXn_ThAACDNJj9IyHdHnHE2Y7dKQGUqRZmJpcSAACrRAAAtdabQSEaZvr0oENsy4E",
    "CAACAgQAAx0CXn_ThAACDNNj9IyHipfhlSYcQzejcQR72ebEywACrhAAAtdabQRFhA5qSFx--C4E",
)

PM_START_TEXT = """
────「 [{}](https://te.legra.ph/file/9b747e295b8f8288ebe5c.jpg) 」────
*Hey Prince Is Here! {},*
*I am an Anime Themed Advance Group Management Bot With Lot Of Cool Features.*
➖➖➖➖➖➖➖➖➖➖➖➖➖
❍ *Uptime ~* `{}`
❍ `{}` *Users, Across* `{}` *Chats.*
➖➖➖➖➖➖➖➖➖➖➖➖➖
❍ *Latest Update ~* 2/21/23
❍ *Version Name ~* Pro Version
➖➖➖➖➖➖➖➖➖➖➖➖➖
❍ *Next Version Update ~* 3/19/23
❍ *Next Version Name ~* Ultimate Version
➖➖➖➖➖➖➖➖➖➖➖➖➖
➪ Hit The *Help* Button Below To Know My Powers ××
"""

buttons = [
    [
        InlineKeyboardButton(
            text=f"Add {BOT_NAME} To Your Group",
            url=f"https://telegram.dog/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="🎗️ Help", callback_data="help_back"),
        InlineKeyboardButton(
            text="Source Code 🖤",
            url=f"https://github.com/Awesome-Gtash/OrekiRobot-3.git",
        ),
    ],
    [
        InlineKeyboardButton(
            text="🚑 Support", url=f"https://telegram.dog/Gtash_Association"
        ),
        InlineKeyboardButton(
            text="📢 Updates", url=f"https://telegram.dog/Gtash_Updates"
        ),
    ],
    [
        InlineKeyboardButton(
            text="My Master 💌", url=f"https://telegram.dog/Awesome_Gtashxd"
        ),
    ],
]

HELP_STRINGS = """
Hey, your *Prince* Is here!
I Help Admins To Manage Their Groups!
*Main* commands available: 
➪ /help: PM's you this message.
➪ /help <module name>: PM's you info about that module.
➪ /donate: information on how to donate!
➪ /settings:
   ➪ in PM: will send you your settings for all supported modules.
   ➪ in a group: will redirect you to pm, with all that chat's settings.
"""

GROUP_START_IMG = (
    "https://te.legra.ph/file/5daed3fffea5dace6bdf6.mp4",
    "https://te.legra.ph/file/b9cf9f626f8c5e44791d9.mp4",
    "https://te.legra.ph/file/e6cdb76fc7e86d83b97d5.mp4",
    "https://te.legra.ph/file/41d159193b7169d71b6a4.mp4",
    "https://te.legra.ph/file/5ab83524f880813db5b9e.mp4",
    "https://te.legra.ph/file/8d08411d24225176e28cd.mp4",
    "https://te.legra.ph/file/7bb995073f9e1bab6ca88.mp4",
)

DONATE_STRING = """❂ I'm Free for Everyone ❂"""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}
GDPR = []

for module_name in ALL_MODULES:
    imported_module = importlib.import_module(f"OrekiRobot.modules.{module_name}")

    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


# do not async
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    OREKI_MOD.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )


def test(update: Update):
    # pprint(eval(str(update)))
    # update.effective_message.reply_text("Hola tester! _I_ *have* `markdown`", parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("This person edited a message")
    print(update.effective_message)


def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="[► Back ◄]", callback_data="help_back"
                                )
                            ]
                        ]
                    ),
                )

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = OREKI_MOD.bot.getChat(match[1])

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match[1], update.effective_user.id, False)
                else:
                    send_settings(match[1], update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            update.effective_message.reply_sticker(
                random.choice(OREKI_STICKERS),
                timeout=60,
            )
            first_name = update.effective_user.first_name
            update.effective_message.reply_text(
                PM_START_TEXT.format(
                    escape_markdown(context.bot.first_name),
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats(),
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
            )
    else:
        update.effective_message.reply_animation(
            random.choice(GROUP_START_IMG),
            caption=f"<b>Hola, I'm awake already!\nOreki Is Here since</b>: <code>{}</code>",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="📢 Updates",
                            url="https://telegram.dog/Dev_Updates",
                        ),
                    ]
                ]
            ),
        )


def error_handler(update: Update, context: CallbackContext):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = f"An exception was raised while handling an update\n<pre>update = {html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False))}</pre>\n\n<pre>{html.escape(tb)}</pre>"

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    OREKI_MOD.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


# for test purposes
def error_callback(_, context: CallbackContext):
    try:
        raise context.error
    except (BadRequest):
        pass
        # remove update.message.chat_id from conversation list
    except TimedOut:
        pass
        # handle slow connection problems
    except NetworkError:
        pass
        # handle other connection problems
    except ChatMigrated:
        pass
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        pass
        # handle all other telegram related errors


def help_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    with contextlib.suppress(BadRequest):
        if mod_match:
            module = mod_match[1]
            text = (
                f"╔═━「 *{HELPABLE[module].__mod_name__}* module: 」\n"
                + HELPABLE[module].__help__
            )

            query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="[► Back ◄]", callback_data="help_back"
                            ),
                            InlineKeyboardButton(
                                text="[► Support ◄]",
                                url=f"https://t.me/Gtash_Association",
                            ),
                        ]
                    ]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match[1])
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, HELPABLE, "help")
                ),
            )

        elif next_match:
            next_page = int(next_match[1])
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")
                ),
            )

        elif back_match:
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")
                ),
            )

        # ensure no spinny white circle
        context.bot.answer_callback_query(query.id)
        # query.message.delete()


def oreki_callback_data(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    uptime = get_readable_time((time.time() - StartTime))
    if query.data == "oreki_":
        query.message.edit_text(
            text="""CallBackQueriesData Here""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="[► Back ◄]", callback_data="oreki_back")]]
            ),
        )
    elif query.data == "oreki_back":
        first_name = update.effective_user.first_name
        query.message.edit_text(
            PM_START_TEXT.format(
                escape_markdown(context.bot.first_name),
                escape_markdown(first_name),
                escape_markdown(uptime),
                sql.num_users(),
                sql.num_chats(),
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,
            disable_web_page_preview=False,
        )


def get_help(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        update.effective_message.reply_photo(
            HELP_IMG,
            HELP_MSG,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Open In Private Chat",
                            url=f"t.me/{OREKI_MOD.bot.username}?start=help",
                        )
                    ]
                ]
            ),
        )

        return

    if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = f" 〔 *{HELPABLE[module].__mod_name__}* 〕\n{HELPABLE[module].__help__}"

        send_help(
            chat.id,
            text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="[► Back ◄]", callback_data="help_back")]]
            ),
        )

    else:
        send_help(chat.id, HELP_STRINGS)


def send_settings(context: CallbackContext, chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join(
                f"*{mod.__mod_name__}*:\n{mod.__user_settings__(user_id)}"
                for mod in USER_SETTINGS.values()
            )

            OREKI_MOD.bot.send_message(
                user_id,
                "These are your current settings:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            OREKI_MOD.bot.send_message(
                user_id,
                "Seems like there aren't any user specific settings available :'(",
                parse_mode=ParseMode.MARKDOWN,
            )

    elif CHAT_SETTINGS:
        chat_name = OREKI_MOD.bot.getChat(chat_id).title
        OREKI_MOD.bot.send_message(
            user_id,
            text=f"Which module would you like to check {chat_name}'s settings for?",
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
            ),
        )
    else:
        OREKI_MOD.bot.send_message(
            user_id,
            "Seems like there aren't any chat settings available :'(\nSend this "
            "in a group chat you're admin in to find its current settings!",
            parse_mode=ParseMode.MARKDOWN,
        )


def settings_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user = update.effective_user
    bot = context.bot
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match[1]
            module = mod_match[2]
            chat = bot.get_chat(chat_id)
            text = f"*{escape_markdown(chat.title)}* has the following settings for the *{CHAT_SETTINGS[module].__mod_name__}* module:\n\n" + CHAT_SETTINGS[
                module
            ].__chat_settings__(
                chat_id, user.id
            )

            try:
                keyboard = CHAT_SETTINGS[module].__chat_settings_buttons__(
                    chat_id, user.id
                )
            except AttributeError:
                keyboard = []
            kbrd = InlineKeyboardMarkup(
                InlineKeyboardButton(text="Back", callback_data=f"stngs_back({chat_id}")
            )
            keyboard.append(kbrd)
            query.message.edit_text(
                text=text, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard
            )
        elif prev_match:
            chat_id = prev_match[1]
            curr_page = int(prev_match[2])
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                f"Hi there! There are quite a few settings for {chat.title} - go ahead and pick what you're interested in.",
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        curr_page - 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif next_match:
            chat_id = next_match[1]
            next_page = int(next_match[2])
            chat = bot.get_chat(chat_id)
            query.message.edit_text(
                f"Hi there! There are quite a few settings for {chat.title} - go ahead and pick what you're interested in.",
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        next_page + 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif back_match:
            chat_id = back_match[1]
            chat = bot.get_chat(chat_id)
            query.message.edit_text(
                text=f"Hi there! There are quite a few settings for {escape_markdown(chat.title)} - go ahead and pick what you're interested in.",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
    except BadRequest as excp:
        if excp.message not in [
            "Message is not modified",
            "Query_id_invalid",
            "Message can't be deleted",
        ]:
            LOGGER.exception("Exception in settings buttons. %s", str(query.data))


def get_settings(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    # ONLY send settings in PM
    if chat.type == chat.PRIVATE:
        send_settings(chat.id, user.id, True)

    elif is_user_admin(update, user.id):
        text = "Click here to get this chat's settings, as well as yours."
        msg.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Settings",
                            url=f"https://telegram.dog/{OREKI_MOD.bot.username}?start=stngs_{chat.id}",
                        )
                    ]
                ]
            ),
        )

    else:
        text = "Click here to check your settings."


def donate(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat  # type: Optional[Chat]
    if chat.type == "private":
        update.effective_message.reply_text(
            DONATE_STRING, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )

        if OWNER_ID != 5189767566 and DONATION_LINK:
            update.effective_message.reply_text(
                f"You can also donate to the person currently running me [here]({DONATION_LINK})",
                parse_mode=ParseMode.MARKDOWN,
            )


    else:
        user = update.effective_message.from_user
        bot = context.bot
        try:
            bot.send_message(
                user.id,
                DONATE_STRING,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
            )

            update.effective_message.reply_text(
                text="I'm free for everyone❤️\njust donate by subs channel, Don't forget to join the support group.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="📢 Updates",
                                url="https://telegram.dog/Dev_Updates",
                            ),
                            InlineKeyboardButton(
                                text="🚑 Support",
                                url=f"https://telegram.dog/Dev_SupportChat",
                            ),
                        ]
                    ]
                ),
            )
        except Unauthorized:
            update.effective_message.reply_text(
                "Contact me in PM first to get donation information."
            )


def migrate_chats(update: Update):
    msg = update.effective_message
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return


    LOGGER.info("Migrating from %s, to %s", old_chat, new_chat)
    for mod in MIGRATEABLE:
        with contextlib.suppress(KeyError, AttributeError):
            mod.__migrate__(old_chat, new_chat)
    LOGGER.info("Successfully migrated!")


def main():
    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            OREKI_MOD.bot.sendMessage(
                f"@{SUPPORT_CHAT}",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="[► Click Here ◄]", url=f"https://t.me/Galaxy_Tamil"
                            ),
                        ]
                    ]
                ),
            )
        except Unauthorized:
            update.effective_message.reply_text(
                "Contact me in PM first to get donation information."
            )
            
            
        def migrate_chats(update: Update):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", old_chat, new_chat)
    for mod in MIGRATEABLE:
        with contextlib.suppress(KeyError, AttributeError):
            mod.__migrate__(old_chat, new_chat)
    LOGGER.info("Successfully migrated!")


def main():
    test_handler = CommandHandler("test", test, run_async=True)
    start_handler = CommandHandler("start", start, run_async=True)

    help_handler = CommandHandler("help", get_help, run_async=True)
    help_callback_handler = CallbackQueryHandler(
        help_button, pattern=r"help_.*", run_async=True
    )

    settings_handler = CommandHandler("settings", get_settings)
    settings_callback_handler = CallbackQueryHandler(
        settings_button, pattern=r"stngs_", run_async=True
    )

    data_callback_handler = CallbackQueryHandler(
        oreki_callback_data, pattern=r"oreki_", run_async=True
    )
    donate_handler = CommandHandler("donate", donate, run_async=True)
    migrate_handler = MessageHandler(
        Filters.status_update.migrate, migrate_chats, run_async=True
    )

    OREKI_MOD.add_handler(start_handler)
    OREKI_MOD.add_handler(help_handler)
    OREKI_MOD.add_handler(data_callback_handler)
    OREKI_MOD.add_handler(settings_handler)
    OREKI_MOD.add_handler(help_callback_handler)
    OREKI_MOD.add_handler(settings_callback_handler)
    OREKI_MOD.add_handler(migrate_handler)
    OREKI_MOD.add_handler(donate_handler)

    OREKI_MOD.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN, certificate=open(CERT_PATH, "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info(
            f"Prince oreki started, Using long polling."
        )
        updater.start_polling(
            timeout=15,
            read_latency=4,
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES,
        )

    if len(argv) in {1, 3, 4}:
        tbot.run_until_disconnected()

    else:
        tbot.disconnect()
    updater.idle()


"""
try:
    ubot.start()
except BaseException:
    print("Userbot Error! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)
"""

PHOTO = "https://te.legra.ph/file/9b747e295b8f8288ebe5c.jpg"

OREKI_START = f"""
[Prince Oreki 왕자]({BOT_USERNAME}) Is Started!

♡︎ Version Name: Pro Version
♡︎ Pyrogram Version: {pyrover}
♡︎ Telethon Version: {tlhver}
"""
INLINE_BUTTON = [
    [                  
        Button.url("Stats🎗", "https://t.me/OrekiProXBot?start=stats_callback"),
    ] 
]
if __name__ == "__main__":
    LOGGER.info(f"Successfully loaded modules: {str(ALL_MODULES)}")
    tbot.start(bot_token=TOKEN)
    tbot.send_file(-1001585435524, PHOTO, caption=OREKI_START, buttons=INLINE_BUTTON)
    pgram.start()
    main()
    idle()
