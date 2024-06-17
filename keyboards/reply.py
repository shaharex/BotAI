from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardRemove
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="How?"),
            KeyboardButton(text="Learn More About It:")
        ],
        [
            KeyboardButton(text="Subjects"),
            KeyboardButton(text="Special buttons")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Choose options from Menu",
    selective=True
)

spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send Geolocation", request_location=True),
            KeyboardButton(text="Send Contact", request_contact=True),
            KeyboardButton(text="Create smth", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="Exit")
        ]
    ],
    resize_keyboard=True
)

rmk = ReplyKeyboardRemove()
