import logging
from config import admin_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_datas import menu_callbacks
from keyboards.inline.choice_buttons import poster_menu, start_menu
from loader import dp, bot
from loguru import logger

logger.add(f'log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')



#@dp.callback_query_handler(menu_callbacks.filter(click1='newsposter'), state=Start.Start_menu)  # Ловим State и callback
#async def news_poster_menu(call: CallbackQuery, state: FSMContext):
#    await state.get_state()
#    text = 'С чем проблемы?'
#    # Меняем текст в сообщении
#    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=text)
#    # Меняем клавиатуру в сообщении
#    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=poster_menu)
#    await NewsPoster.Choise_command.set()
#
#
#@dp.callback_query_handler(state=NewsPoster.Choise_command)
#async def news_poster(call: CallbackQuery, state: FSMContext):
#    button_callback = call.data.split(':')[1]
#    if button_callback == 'Back':
#        text = 'Привет! Выбирай кнопку'
#        # Меняем текст в сообщении
#        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=text)
#        # Меняем клавиатуру в сообщении
#        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=start_menu)
#        await state.get_state()
#        await Start.first()
