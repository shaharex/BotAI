from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from keyboards.inline import sub_channel


class CheckSubsription(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member("@hunshasha", event.from_user.id)

        if chat_member.status != "left":
            return await handler(event, data)
        else:
            await event.answer(
                "Subscribe to channel, to get access to bot!",
                reply_markup=sub_channel
            )