# handlers.py
from aiogram import types
from db import insert_data
from ui import get_questions_menu, get_main_menu
from popular_questions import get_popular_questions

async def handle_questions_menu(message: types.Message):
    """Обработка раздела 'Вопросы по заказу'."""
    if message.text == "Самые популярные вопросы":
        # Получаем популярные вопросы
        questions = get_popular_questions()
        response = "\n\n".join(questions)
        await message.answer(f"Самые популярные вопросы:\n\n{response}")
    elif message.text == "Назад":
        # Возвращаемся в главное меню
        await message.answer("Вы вернулись в главное меню.", reply_markup=get_main_menu())

        
async def handle_menu(message: types.Message, user_data):
    """Обработка выбора из меню"""
    user_id = message.chat.id
    user_data[user_id] = {"step": message.text, "data": {}}
    
    if message.text == "💵Оформление заказа💵":
        await message.answer("Введите ваше ФИО:")
    elif message.text == "🛎️Информация по заказу🛎️":
        await message.answer("Введите ваше ФИО:")
    elif message.text == "📑Ваши данные📑":
        await message.answer("Введите ваше ФИО:")
    elif message.text == "💰Наличие и цена🚚":
        await message.answer("Введите ваше ФИО:")

async def collect_data(message: types.Message, user_data):
    """Сбор данных пользователя"""
    user_id = message.chat.id
    if user_id not in user_data or not user_data[user_id]["step"]:
        await message.answer("Пожалуйста, выберите действие из меню:", reply_markup=get_main_menu())
        return

    step = user_data[user_id]["step"]
    data = user_data[user_id]["data"]

    # Отладочное сообщение: текущий шаг и данные
    print(f"Шаг: {step}, Данные: {data}")

    # Логика для "Оформление заказа"
    if step == "💵Оформление заказа💵":
        if "fio" not in data:
            data["fio"] = message.text
            print(f"Получено ФИО: {data['fio']}")
            await message.answer("Введите ваш номер телефона:")
        elif "phone" not in data:
            data["phone"] = message.text
            print(f"Получен телефон: {data['phone']}")
            await message.answer("Введите ваш адрес:")
        elif "adres" not in data:
            data["adres"] = message.text
            print(f"Получен adres: {data['adres']}")
            
            # Попытка записи данных в таблицу orders
            try:
                insert_data("orders", data)
                print(f"Данные записаны в таблицу orders: {data}")
                user_data[user_id] = {"step": None, "data": {}}
                await message.answer("Ваш заказ успешно оформлен! Спасибо!", reply_markup=get_main_menu())
                await message.answer("Вы можете выбрать другое действие:", reply_markup=get_main_menu())

            except Exception as e:
                print(f"Ошибка при записи в базу: {e}")
                await message.answer("Произошла ошибка при записи данных. Попробуйте позже.")

    # Логика для "Информация по заказу"
    elif step == "🛎️Информация по заказу🛎️":
        if "fio" not in data:
            data["fio"] = message.text
            print(f"Получено ФИО для вопросов: {data['fio']}")
            await message.answer("Введите ваш номер телефона для связи:")
        elif "phone" not in data:
            data["phone"] = message.text
            print(f"Получен телефон для вопросов: {data['phone']}")
            await message.answer("Введите ваш adres для связи:")
        elif "adres" not in data:
            data["adres"] = message.text
            print(f"Получен adres для вопросов: {data['adres']}")
            
            # Запись данных в таблицу questions
            try:
                insert_data("questions", data)
                print(f"Данные записаны в таблицу questions: {data}")
                user_data[user_id] = {"step": None, "data": {}}
                await message.answer("Ваш запрос по заказу успешно отправлен! Спасибо!", reply_markup=get_main_menu())
                await message.answer("Вы можете выбрать другое действие:", reply_markup=get_main_menu())

            except Exception as e:
                print(f"Ошибка при записи в базу: {e}")
                await message.answer("Произошла ошибка при записи данных. Попробуйте позже.")
    
    # Логика для "Ваши данные"
    elif step == "📑Ваши данные📑":
        if "fio" not in data:
            data["fio"] = message.text
            print(f"Получено ФИО для бухгалтерии: {data['fio']}")
            await message.answer("Введите ваш номер телефона:")
        elif "phone" not in data:
            data["phone"] = message.text
            print(f"Получен телефон для бухгалтерии: {data['phone']}")
            await message.answer("Введите ваш adres:")
        elif "adres" not in data:
            data["adres"] = message.text
            print(f"Получен adres для бухгалтерии: {data['adres']}")
            
            # Запись данных в таблицу accounting
            try:
                insert_data("accounting", data)
                print(f"Данные записаны в таблицу accounting: {data}")
                user_data[user_id] = {"step": None, "data": {}}
                await message.answer("Ваш запрос на Ваши данные успешно отправлен! Спасибо!", reply_markup=get_main_menu())
                await message.answer("Вы можете выбрать другое действие:", reply_markup=get_main_menu())

            except Exception as e:
                print(f"Ошибка при записи в базу: {e}")
                await message.answer("Произошла ошибка при записи данных. Попробуйте позже.")
    
    # Логика для "Наличие и цена"
    if step == "💰Наличие и цена💰":
        if "fio" not in data:
            data["fio"] = message.text
            print(f"Получено ФИО для поставщика: {data['fio']}")
            await message.answer("Введите ваш номер телефона:")
        elif "phone" not in data:
            data["phone"] = message.text
            print(f"Получен телефон для поставщика: {data['phone']}")
            await message.answer("Введите ваш adres:")
        elif "adres" not in data:
            data["adres"] = message.text
            
            # Запись данных в таблицу suppliers
            try:
                print(f"Перед записью в базу данных: {data}")  # Отладочное сообщение
                insert_data("suppliers", data)
                print(f"Данные записаны в таблицу suppliers: {data}")
                user_data[user_id] = {"step": None, "data": {}}
                await message.answer("Ваш запрос стать поставщиком успешно отправлен! Спасибо!", reply_markup=get_main_menu())
                await message.answer("Вы можете выбрать другое действие:", reply_markup=get_main_menu())

            except Exception as e:
                print(f"Ошибка при записи в базу: {e}")
                await message.answer("Произошла ошибка при записи данных. Попробуйте позже.")