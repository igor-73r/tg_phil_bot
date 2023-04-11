import telebot
import features
from config import *
import keyboards
import library

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот философ, который поможет тебе "
                          "погрузиться в мир философии!".format(message.from_user))
    bot.send_message(message.chat.id, text="Введите возраст читателя")
    bot.register_next_step_handler(message, features.get_age)


@bot.callback_query_handler(func=lambda call: call.data.startswith('show_books_'))
def call_back(call):
    library.show_books(call)


@bot.callback_query_handler(func=lambda call: call.data.startswith('show_book_'))
def call_back(call):
    library.show_book(call)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    message_id = message.message_id

    match message.text.lower():
        case "начать":
            bot.send_message(chat_id=chat_id, text="Отлично! Вот что я нашел для тебя:",
                             reply_markup=keyboards.default_keyboard)
            features.build(chat_id=chat_id, user_id=user_id)

        case "далее":
            features.build(chat_id=chat_id, user_id=user_id)

        case "настройки":
            bot.send_message(chat_id=chat_id, text="Настройки",
                             reply_markup=keyboards.settings_keyboard)
            bot.delete_message(chat_id=chat_id, message_id=message_id)

        case "показать библиотеку":
            bot.send_message(chat_id=chat_id, text="Библиотека",
                             reply_markup=library.get_inline_keyboard())

        case "назад":
            bot.send_message(chat_id=chat_id, text="Назад",
                             reply_markup=keyboards.default_keyboard)
            bot.delete_message(chat_id=chat_id, message_id=message_id)

        case "изменить возраст":
            bot.send_message(chat_id=chat_id, text="Введите возраст читателя")
            bot.register_next_step_handler(message, features.get_age)

        case _:
            bot.send_message(chat_id=chat_id, text="Сударь, я вас не понимаю")


bot.polling(none_stop=True, interval=0)
