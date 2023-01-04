from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from lexicon_ru import LEXICON_RU
from keyboards import yes_no_kb, game_kb
from services import get_bot_choice, get_winner


async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_yes_answer,
                                text=LEXICON_RU['yes_button'])
    dp.register_message_handler(process_no_answer,
                                text=LEXICON_RU['no_button'])
    dp.register_message_handler(process_game_button,
                                Text(equals=[LEXICON_RU['rock'],
                                             LEXICON_RU['paper'],
                                             LEXICON_RU['scissors']]))