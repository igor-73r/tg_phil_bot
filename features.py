from config import *
import telebot
import db_worker

bot = telebot.TeleBot(TOKEN)


def get_age(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Начать")
    markup.add(btn1)
    try:
        age = int(message.text)
        db_worker.new_user(user_id=message.from_user.id, age=age)
        bot.reply_to(message, "Спасибо! Ваш возраст сохранен.", reply_markup=markup)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введи число.")
