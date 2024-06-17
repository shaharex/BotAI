import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.scene import SceneRegistry
from aiogram.fsm.storage.memory import SimpleEventIsolation

from handlers import bot_messages, user_commands, questionare
from callbacks import pagination
from scene import scene_question


from midlewares.check_sub import CheckSubsription
from midlewares.antiflood import AntiFloodMiddleware
from scene.scene_question import QuizScene

from config_reader import config


async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher(
        events_isolation=SimpleEventIsolation()
    )

    dp.message.middleware(CheckSubsription())
    dp.message.middleware(AntiFloodMiddleware())

    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionare.router,
        bot_messages.router
    )

    dp.include_router(scene_question.router)

    scene_registry = SceneRegistry(dp)
    scene_registry.add(QuizScene)

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())