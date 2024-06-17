from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply, inline, builders, fabrics
from data.subloader import get_json

router = Router()


@router.message(F.text.lower().in_(["student", "education", "bot"]))
async def greetings(message: Message):
    await message.reply("☃️ @againsthun_bot - Uniting Students, One Chat at a Time! 🌍")


@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json("smiles.json")

    if msg == "learn more about it:":
        await message.answer("Great that you want to learn more.We are here to provide you with more information and resources.Here are some ways you can learn more:", reply_markup=inline.links)
    elif msg == "special buttons":
        await message.answer("Special buttons", reply_markup=reply.spec)
    elif msg == "subjects":
        await message.answer("You can choose subjects and see available courses", reply_markup=builders.calc())
    elif msg == "how?":
        await message.answer(f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator())
    elif msg == "exit":
        await message.answer("you are returned to main menu!", reply_markup=reply.main)

