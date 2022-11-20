from OrekiRobot import OREKI_MOD
from OrekiRobot.modules.disable import DisableAbleCommandHandler
from OrekiRobot.modules.helper_funcs.alternate import send_message
from OrekiRobot.modules.helper_funcs.chat_status import dev_plus


@dev_plus
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send, run_async=True)
OREKI_MOD.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [ADD_CCHAT_HANDLER]
