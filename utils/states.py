from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    Your_Name = State()
    Your_Age = State()
    Your_Gender = State()
    About_You = State()
    Your_Photo = State()


class Feedback(StatesGroup):
    Your_name = State()
    Your_feedback = State()
    Some_updates = State()