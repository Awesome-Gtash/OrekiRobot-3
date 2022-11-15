"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022-2023, Awesome-Gtash, [ https://github.com/Awesome-Gtash ]
Copyright (c) 2022-2023, White Tiger • Network, [ https://github.com/Awesome-Gtash/OrekiRobot-3 ]
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import contextlib
import html
import importlib
import json
import random
import re
import time
import traceback
from sys import argv
from typing import Optional

from pyrogram import idle
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import escape_markdown

import OrekiRobot.modules.sql.users_sql as sql
from OrekiRobot import (
    BOT_NAME,
    BOT_USERNAME,
    DONATION_LINK,
    HELP_IMG,
    LOGGER,
    NEKO_PTB,
    OWNER_ID,
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

NEKO_STICKERS = (
    "CAACAgQAAx0Cb_P9BQACFsdjUVxcW5w3HTH1k0dJWX172OVYSQACiggAAk3XEFKGGWr9yYBHjioE",
    "CAACAgQAAx0Cb_P9BQACFtBjUV2Z2ptlwcaQIFz0aCvl2DLPzQACnwoAAnulCFJnpb4Q4L3qZSoE",
    "CAACAgQAAx0Cb_P9BQACFttjUV3JS-Ma9JKJxYTIWKsidqogaAACnwcAAthvEFIVm9fgYJwwOCoE",
    "CAACAgQAAx0Cb_P9BQACFuRjUV4ChyAN5IpndbVzhHqpga3M6gACGwgAAqDQEVJKBbDANRJGryoE",
    "CAACAgQAAx0Cb_P9BQACFu1jUV4ldIfUKtqqINPTzD6NdhzOQQACvQ8AAiPoCFIw05rlLfpZpyoE",
)

PM_START_TEXT = """
────「 [{}](https://te.legra.ph/file/5aadfffa390146c1fb9a2.jpg) 」────
*Hey Prince Is Here! {},*
*I am an Anime Themed Advance Group Management Bot With Lot Of Cool Features.*
➖➖➖➖➖➖➖➖➖➖➖➖➖
➪ *Uptime:* `{}`
➪ *Python:* 3.10.8
➪ `{}` *Users, Across* `{}` *Chats.*
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
            url=f"https://github.com/Awesome-Gtash/OrekiRobot-2.git",
        ),
    ],
    [
        InlineKeyboardButton(
            text="🚑 Support", url=f"https://telegram.dog/Tiger_SupportChat"
        ),
        InlineKeyboardButton(
            text="📢 Updates", url=f"https://telegram.dog/Tiger_Updates"
        ),
    ],
    [
        InlineKeyboardButton(
            text="My Master 💌", url=f"https://telegram.dog/Awesome_MB"
        ),
    ],
]

HELP_STRINGS = """
────「 [Prince Oreki 왕자](https://te.legra.ph/file/39b288a934734512d98e5.jpg) 」────
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
    OREKI_PTB.bot.send_message(
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
                chat = NEKO_PTB.bot.getChat(match[1])

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
            caption=f"<b>Hola, I'm awake already!\nOreki Is Here since</b>: <code>{uptime}</code>",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="📢 Updates",
                            url="https://telegram.dog/Tiger_Updates",
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
    OREKI_PTB.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


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
                                url=f"https://t.me/Tiger_SupportChat",
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
                            url=f"t.me/{OREKI_PTB.bot.username}?start=help",
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
