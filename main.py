import telebot
import db_worker
import features
from config import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот философ, который поможет тебе "
                          "погрузиться в мир философии!".format(message.from_user))
    bot.send_message(message.chat.id, text="Введите возраст читателя")
    bot.register_next_step_handler(message, features.get_age)


@bot.message_handler(content_types=['text'])
def func(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    done = telebot.types.KeyboardButton("Далее")
    markup.add(done)
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.text.lower() == "начать":
        bot.send_message(message.chat.id, text="Отлично! Вот что я нашел для тебя:", reply_markup=markup)
        build(chat_id, user_id)

    elif message.text.lower() == "далее":
        build(chat_id, user_id)

    else:
        bot.send_message(message.chat.id, text="Сударь, я вас не понимаю")


def build(chat_id, user_id):
    temp = db_worker.parse_to_message(user_id)
    if temp:
        name, description, author, file = temp
        bot.send_photo(chat_id=chat_id, photo=open(f"covers/{file}.jpg", "rb"),
                       caption=f"{name}\nАвтор: {author}\nОписание: {description}")
        bot.send_document(chat_id=chat_id, document=open(f"books/{file}.fb2", "rb"))
    else:
        bot.send_message(chat_id=chat_id, text="На этом пока все, приходите позже")


bot.polling(none_stop=True, interval=0)
