from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def inline_builder(
        text: str | list[str],
        callback_data: str | list[str],
        sizes: int | list[int]= 2,
        **kwargs
) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(callback_data, str):
        callback_data = [callback_data]
    if isinstance(sizes, str):
        sizes = [sizes]

    [
        builder.button(text=txt, callback_data=cb)
        for txt, cb in zip(text, callback_data)
    ]

    builder.adjust(*sizes)
    return builder.as_markup(**kwargs)


def calc():
    items = [
        "math", "chem", "geo",
        "eng", "phys", "hist",
        "scie", "econ", "info"
    ]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Exit")
    builder.adjust(*[3] * 3)

    return builder.as_markup(resize_keyboard=True)


def profile(text: str | list):
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)