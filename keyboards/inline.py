from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit Website", url="https://au.int/en/overview"),
        InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=Africaunitebch"),
        InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/@AUCommission"),
        InlineKeyboardButton(text="See the document version", url="https://docs.aiogram.dev/en/latest/")
    ]
    ]
)

sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="subscribe", url="https://t.me/hunshasha")
        ]
    ]
)