from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    """Главное меню."""
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(KeyboardButton("💵Оформление заказа💵"))
    menu.add(KeyboardButton("🛎️Информация по заказу🛎️"))
    menu.add(KeyboardButton("📑Ваши данные📑"))
    menu.add(KeyboardButton("💰Наличие и цена💰"))

    return menu


def get_questions_menu():
    # Реализация функции
    pass

