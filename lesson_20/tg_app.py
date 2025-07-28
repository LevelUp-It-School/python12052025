import telebot
from telebot import types

bot = telebot.TeleBot("8434991165:AAGYzp8ewqTZe4nTWRmvkO8FXZgeIibmikk")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Кнопка приветствия🐯")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, я бот помощник LevelUp🤩", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "Кнопка приветствия🐯":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как проходит обучение?")
        btn2 = types.KeyboardButton("Контакты")
        btn3 = types.KeyboardButton("Расписание")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Задайте интересующий вас вопрос❓", reply_markup=markup)
    elif message.text == "Как проходит обучение?":
        bot.send_message(message.from_user.id, "Посмотреть информацию об онлайн обучении можно по [ссылке](https://levelp.ru/courses/webinars/", parse_mode="Markdown")
    elif message.text == "Контакты":
        bot.send_message(message.from_user.id, "Посмотреть контактную информацию можно по [ссылке](https://levelp.ru/contacts/", parse_mode="Markdown")
    elif message.text == "Расписание":
        bot.send_message(message.from_user.id, "Посмотреть информацию о расписании можно по [ссылке](https://levelp.ru/courses/schedule/", parse_mode="Markdown")

bot.infinity_polling()

"""
Напишите класс Character обладающий 3 характеристиками: атака, здоровье, уклонение
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

Класс имеет следующие методы:
Распределение атрибутов как описано выше: character_1 = Character("fighter")
Атака
Получение урона в случае если увернуться не удалось.
Уклонение: каждое очко уклонения умножается на 5. Результат уклонения зависит от рандомно генерируемого числа
от 0 до 100. Если это число меньше или равно навыка уклонения, то герой уклоняется от атаки.
Смерть: если здоровье меньше 1.

Напишите функцию которая заставит сразиться разных героев друг с другом 100 раз. Выведите счет.
"""

