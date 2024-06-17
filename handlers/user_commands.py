import random
import asyncio
import io
import csv
import aiohttp
import openai
import os
from openai import OpenAI

from aiogram import Router, Bot, F, types
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.utils import markdown
from aiogram.enums import ChatAction

from keyboards import reply

from filters.is_admin import IsAdmin
from filters.is_digit_or_float import CheckForDigit

router = Router()

openai.api_key = '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'

os.environ["OPENAI_API_KEY"] = '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'

client = OpenAI()


@router.message(Command("ai_poem_new"))
async def send(message: Message):

    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(7)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a poetic assistant, write poem about New Year in College"},
            {"role": "user", "content": "Compose a poem that explains how the New Year is celebrating in College"}
        ]
    )
#
    await message.answer(completion.choices[0].message.content, reply_markup=reply.main)

#
# @router.message(Command("ai_poem"))
# async def send(message: Message):
#
#     await message.bot.send_chat_action(
#         chat_id=message.chat.id,
#         action=ChatAction.TYPING
#     )
#     await asyncio.sleep(7)
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system",
#              "content": "You are a poetic assistant, write poem about Students"},
#             {"role": "user", "content": "Compose a poem that explains how the students live nowadays"}
#         ]
#     )
#
#     await message.answer(completion.choices[0].message.content, reply_markup=reply.main)
#
@router.message(Command("help"))
async def send(message: Message):

    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(7)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a help-assistant for students, give the information about how to use bot"},
            {"role": "user", "content": "Compose a shortest information that provide how to use bot"}
        ]
    )

    await message.answer(completion.choices[0].message.content, reply_markup=reply.main)


# @router.message(F.text.lower().in_(["cat", "kitty"]))
# async def send(message: Message):
#     await message.bot.send_chat_action(
#         chat_id=message.chat.id,
#         action=ChatAction.TYPING
#     )
#     await asyncio.sleep(7)
#     byte_stream: BytesIO = [your image data]
#     byte_array = byte_stream.getvalue()
#     response = client.images.(
#         model="dall-e-3",
#         prompt="a white siamese cat",
#         size="1024x1024",
#         quality="standard",
#         n=1,
#     )
#
#     await message.send_image(response.data[0].url, reply_markup=reply.main)

@router.message(CommandStart(), IsAdmin(1263118338))
async def start(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(1)
    url = "https://images.unsplash.com/photo-1533745848184-3db07256e163?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    await message.answer(f"{markdown.hide_link(url)}Hello, <b><i>{message.from_user.first_name}</i>.</b> Welcome to <b>StudentsHelp</b>, your virtual assistant dedicated to fostering students across the world. Our bot is designed to address key challenges and promote collaboration among students.", reply_markup=reply.main)


@router.message(F.from_user.id.in_({42, 1263118338}), F.text == "Who am I?")
async def secret_admin_message(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.FIND_LOCATION
    )
    await asyncio.sleep(2)
    await message.reply("Hi, admin!")


@router.message(Command("pay", prefix="$/"), CheckForDigit())
async def pay_the_order(message: Message) -> None:
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(2)
    await message.answer("The payment was successful")


@router.message(Command("process"))
async def handle_command_pic(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    await asyncio.sleep(2)
    url = "https://images.unsplash.com/photo-1560785496-284e257f0bf7?q=80&w=2835&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    await message.answer_photo(
        photo=url,
        caption=f"<b>Vision Screenings:</b>\n"
        f"Students studying using bot\n"
    )


@router.message(Command(commands=["rn", "studying"]))
async def get_random_number(message: Message, command: CommandObject) -> None:
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(2)
    a, b = [int(n) for n in command.args.split("-")]
    rnum = random.randint(a, b)

    await message.reply(f"People studying right now: {rnum}")


@router.message(Command("students"))
async def send_csv_file(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    await asyncio.sleep(2)
    file = io.StringIO()
    csv_writer = csv.writer(file)
    csv_writer.writerows(
        [
            ["Name", "Age", "City"],
            ["John Smith", "28", "New York"],
            ["Jane Doe", "32", "Los Angeles"],
            ["Mike Johnson", "40", "Chicago"],
            ["shaha", "23", "Taraz"],
            ["beibars", "43", "Almaty"],
            ["yernasip", "35", "Astana"],
            ["yerbol", "21", "Tokyo"]
        ]
    )
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="participants.csv",
        ),
    )


@router.message(Command("file"))
async def handle_command_file(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    await asyncio.sleep(2)
    file_path = "C:/Users/User/Downloads/elon.jpeg"
    await message.reply_document(
        document=types.FSInputFile(
            path=file_path,
            filename="how we give the food"
        )
    )


@router.message(Command("big_file"))
async def send_big_file(message: Message):
    await asyncio.sleep(7)
    file = io.BytesIO()
    url = "https://images.unsplash.com/photo-1695653422259-8a74ffe90401?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_bytes = await response.read()

    file.write(result_bytes)

    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    await asyncio.sleep(2)
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue(),
            filename="the process.jpeg",
        ),
    )


@router.message(Command("test"))
async def test(message: Message, bot: Bot):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(2)
    await bot.send_message(message.chat.id, "how and who")

#
# @router.message()
# async def echo_message(message: Message):
#
#     # if message.text:
#     #     await message.bot.send_chat_action(
#     #         chat_id=message.chat.id,
#     #         action=ChatAction.TYPING
#     #     )
#     #     await asyncio.sleep(2)
#     #     await message.reply(
#     #         text="I don't understand u!",
#     #         parse_mode=None,
#     #     )
#
#     if message.sticker:
#         await message.bot.send_chat_action(
#             chat_id=message.chat.id,
#             action=ChatAction.CHOOSE_STICKER,
#         )
#         await asyncio.sleep(2)
#
#         await message.answer(
#             text="Wait a second...",
#             parse_mode=None
#         )
#         await message.copy_to(chat_id=message.chat.id)


@router.message(F.new_chat_members)
async def somebody_added(message: Message):
    for user in message.new_chat_members:
        await message.reply(f"Welcome, now you have access to bot, {user.full_name}")


@router.message(F.text.lower().in_(["math"]))
async def handle_photo_wo_caption(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    await asyncio.sleep(2)
    caption = "Mathematics is the important"
    await message.reply_photo(
        photo="https://images.unsplash.com/photo-1596495577886-d920f1fb7238?q=80&w=2948&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption=caption
    )


@router.message(F.text.lower().in_(["chem"]))
async def handle_photo_wo_caption(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    await asyncio.sleep(2)
    caption = "Chemistry is also important"
    await message.reply_photo(
        photo="https://images.unsplash.com/photo-1595500381751-d940898d13a0?q=80&w=3028&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption=caption
    )


@router.message(F.text.lower().in_(["geo"]))
async def handle_photo_wo_caption(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    await asyncio.sleep(2)
    caption = "Start quiz with the /scene about Geography"
    await message.reply_photo(
        photo="https://images.unsplash.com/photo-1619469399933-05d6e31688d4?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption=caption
    )


@router.message(F.text.lower().in_(["hist"]))
async def handle_photo_wo_caption(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    await asyncio.sleep(2)
    caption = "Some history courses here: https://www.coursera.org/browse/arts-and-humanities/history"
    await message.reply_photo(
        photo="https://images.unsplash.com/photo-1473163928189-364b2c4e1135?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption=caption
    )

@router.message(F.text.lower().in_(["econ"]))
async def handle_photo_wo_caption(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    await asyncio.sleep(2)
    caption = "Principles of Economics by Mankiw: https://en.wikiversity.org/wiki/10_Principles_of_Economics"
    await message.reply_photo(
        photo="https://images.unsplash.com/photo-1535320903710-d993d3d77d29?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption=caption
    )




