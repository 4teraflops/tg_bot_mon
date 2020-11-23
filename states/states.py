from aiogram.dispatcher.filters.state import StatesGroup, State


class Start(StatesGroup):
    Start_menu = State()


class Pu(Start):
    Tools = State()
    Manage = State()


class ACQPC(Start):
    Tools = State()
    Manage = State()


class NewsPoster(Start):
    Choise_command = State()


class DemoChecker(Start):
    Start = State()