import asyncio

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatAction


from utils.states import Form, Feedback
from keyboards.builders import profile
from keyboards.reply import rmk

router = Router()


@router.message(Command("profile"))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.Your_Name)
    await message.answer(
        "Become a part of people who support us.Let's start, first enter your <b>name</b>",
        reply_markup=profile(message.from_user.first_name)
    )


@router.message(Form.Your_Name)
async def form_name(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.Your_Age)
    await message.answer("Great,now enter your age", reply_markup=rmk)


@router.message(Form.Your_Age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Form.Your_Gender)
        await message.answer(
            "Choose your gender",
            reply_markup=profile(["Male", "Female"])
        )
    else:
        await message.answer("Enter number, again!")


@router.message(Form.Your_Gender, F.text.casefold().in_(["male", "female"]))
async def form_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Form.About_You)
    await message.answer("Tell about yourself", reply_markup=rmk)


@router.message(Form.Your_Gender)
async def incorrect_form_sex(message: Message, state: FSMContext):
    await message.answer("Push button")


@router.message(Form.About_You)
async def form_about(message: Message, state: FSMContext):
    if len(message.text) < 10:
        await message.answer("Write something more interesting")
    else:
        await state.update_data(about=message.text)
        await state.set_state(Form.Your_Photo)
        await message.answer("Now send your photo")


@router.message(Form.Your_Photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
        photo_file_id = message.photo[-1].file_id
        data = await state.get_data()
        await state.clear()

        formatted_text = []
        [
            formatted_text.append(f"{key} : {value}")
            for key, value in data.items()
        ]

        await message.answer_photo(
            photo_file_id,
            "\n".join(formatted_text)
        )


@router.message(Form.Your_Photo, ~F.photo)
async def incorrect_form_photo(message: Message, state:FSMContext):
    await message.answer("Send a photo!")


# Feedback starts here
@router.message(Command("feedback"))
async def fill_feedback(message: Message, state: FSMContext):
    await state.set_state(Feedback.Your_name)
    await message.answer(
        "Let's start with your name",
        reply_markup=profile(message.from_user.first_name)
    )


@router.message(Feedback.Your_name)
async def feed_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Feedback.Your_feedback)
    await message.answer("Great, now write your feedback", reply_markup=rmk)


@router.message(Feedback.Your_feedback)
async def feed_feed(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Feedback.Some_updates)
    if len(message.text) < 5:
        await message.answer("Write real feedback")
    else:
        await message.answer("If you want to suggest some updates, please suggest")


@router.message(Feedback.Some_updates)
async def feed_updates(message: Message, state: FSMContext):
    infor = await state.get_data()
    await state.clear()

    formatted_info = []
    [
        formatted_info.append(f"{key} : {value}")
        for key, value in infor.items()
    ]
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(1)

    caption = "Thank you for your feedback,we will try to improve abilities of our bot"
    await message.answer_photo(
        photo="https://images.unsplash.com/photo-1584890280660-9322ee35baf1?q=80&w=2868&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption=caption
    )


