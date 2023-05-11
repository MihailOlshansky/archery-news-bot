from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram_dialog import DialogRegistry, DialogManager, StartMode

from bot.bot_commands import start_command, put_file_info, put_competition, put_year, add_file_command, \
    get_files_command, put_state, get_state
from bot.common import bot, get_competition_state, get_year_state
from bot.dialogs import main_dialog, add_protocol_dialog, add_rule_dialog, get_protocols_dialog, get_rules_dialog
from bot.stategroups import StatesConstants, MainSG

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)

registry.register(main_dialog)
registry.register(add_protocol_dialog)
registry.register(add_rule_dialog)
registry.register(get_protocols_dialog)
registry.register(get_rules_dialog)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message, dialog_manager: DialogManager):
    await start_command(message, dialog_manager)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def process_put_file_info_command(message: types.Message, dialog_manager: DialogManager):
    state = get_state(dialog_manager)
    if StatesConstants.ADD not in state.state:
        return

    put_file_info(message, dialog_manager)

    put_state(dialog_manager, get_competition_state(state))
    await dialog_manager.reset_stack()
    await message.answer('Введи название соревнования')


@dp.message_handler(content_types=types.ContentType.ANY)
async def process_text_command(message: types.Message, dialog_manager: DialogManager):
    state = get_state(dialog_manager)
    if StatesConstants.COMPETITION in state.state:
        put_competition(message, dialog_manager)
        put_state(dialog_manager, get_year_state(state))
        await dialog_manager.reset_stack()
        await message.answer('Введи год соревнования')
    elif StatesConstants.YEAR in state.state:
        put_year(message, dialog_manager)

        if StatesConstants.ADD in state.state:
            await add_file_command(message, dialog_manager)
        elif StatesConstants.GET in state.state:
            await get_files_command(message, dialog_manager)

        put_state(dialog_manager)
        await message.answer('Чтобы выполнить команду напиши /start')
