import telebot
import features
from config import *
import keyboards

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
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.text.lower() == "начать":
        bot.send_message(message.chat.id, text="Отлично! Вот что я нашел для тебя:",
                         reply_markup=keyboards.default_keyboard)
        features.build(chat_id, user_id)

    elif message.text.lower() == "далее":
        features.build(chat_id, user_id)

    elif message.text.lower() == "настройки":
        bot.send_message(message.chat.id, text="Настройки",
                         reply_markup=keyboards.settings_keyboard)
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == "назад":
        bot.send_message(message.chat.id, text="Назад",
                         reply_markup=keyboards.default_keyboard)
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == "изменить возраст":
        bot.send_message(message.chat.id, text="Введите возраст читателя")
        bot.register_next_step_handler(message, features.get_age)

    else:
        bot.send_message(message.chat.id, text="Сударь, я вас не понимаю")


bot.polling(none_stop=True, interval=0)
