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
    match message.text.lower()[:-2]:
        case "далее":
            features.build(chat_id=chat_id, user_id=user_id)

        case "настройки":
            bot.send_message(chat_id=chat_id, text="⚙️",
                             reply_markup=keyboards.settings_keyboard)

        case "показать библиотеку":
            bot.send_message(chat_id=chat_id, text="Библиотека📚",
                             reply_markup=library.get_inline_keyboard())

        case "на главную":
            bot.send_message(chat_id=chat_id, text="⬅️",
                             reply_markup=keyboards.default_keyboard)

        case "изменить возраст":
            bot.send_message(chat_id=chat_id, text="✏️")
            bot.send_message(chat_id=chat_id, text="Введите возраст")
            bot.register_next_step_handler(message, features.get_age)

        case "авто":
            bot.send_message(chat_id=chat_id, text="❇️",
                             reply_markup=keyboards.auto_keyboard)
            features.build(chat_id=chat_id, user_id=user_id)

        case _:
            bot.send_message(chat_id=chat_id, text="Сударь, я вас не понимаю", reply_markup=keyboards.default_keyboard)


bot.polling(none_stop=True, interval=0)
