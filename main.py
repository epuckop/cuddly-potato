"""
Telegram Bot made by stupid me :)
"""

# Imports
import os, logging, json, datetime, def_list
from pickle import TRUE
from re import IGNORECASE
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot_token   = os.environ['telegram_token']
bot         = Bot(token=bot_token)
dp          = Dispatcher(bot)
dialog_dict = {}

# read approved IDs list
approved_json = json.load(open('approved-ids.json'))
approved_list = []
for element in approved_json:    
    approved_list.append(element['id'])

# Commands handler
@dp.message_handler(commands=['clean'], user_id = approved_list)
async def clean_dialog_state(message: types.Message):
    """
    This handler will be called when approved user run '/clean' command.
    """
    await message.reply(f"Hi {message.from_user.username}, the dialog state is clean")
    dialog_dict = {}


# Message handler
@dp.message_handler(user_id = approved_list)
async def approved_dialog(message: types.Message):
    """
    This handler will be called when accessed by approved user.
    """
    print(message)
    # time validation
    if ():
        pass
    else:
        pass


    # check if has active dialog
    if (str(message.from_user.id) not in dialog_dict):
        dialogtime = datetime.datetime.timestamp(datetime.datetime.now())
        dialog_dict.update({str(message.from_user.id):{'action':'none', 'target':'none', 'approve':'none' ,'time': dialogtime}})
    else:
        pass
    
    # Action key
    match dialog_dict[str(message.from_user.id)]['action']:
        case 'none':
            await message.reply(f"Hi {message.from_user.username}, action in 'none' state")
            dialog_dict[str(message.from_user.id)]['action'] = 'waiting'
            dialog_dict[str(message.from_user.id)]['time'] = datetime.datetime.timestamp(datetime.datetime.now())


@dp.message_handler()
async def not_approved_dialog(message: types.Message):
    """
    This handler will be called when accessed by an approved user.
    """
    await message.reply(f"Hi {message.from_user.username}, you are not approved to use this bot.\nPlease call 03-6005-252 or send email to support@expim.co.il,\nand provide your telegram id: {message.from_user.id}")

    

    

    








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)