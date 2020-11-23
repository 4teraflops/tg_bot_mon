from loader import bot, storage
from src.manager import do_alarm
from loguru import logger

logger.add(f'log/{__name__}.log', format='{time} {level} {message}', level='DEBUG', rotation='10 MB', compression='zip')


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    try:
        executor.start_polling(dp, on_shutdown=on_shutdown)
    except KeyboardInterrupt:
        print('Вы завершили работу программы collector')
        logger.info('Program has been stop manually')
    except Exception as e:
        t_alarmtext = f'tg_mon_bot (app.py): {e}'
        do_alarm(t_alarmtext)
        logger.error(f'Other except error Exception: {e}', exc_info=True)
