from config import *
import telebot
import db_worker
import keyboards

bot = telebot.TeleBot(TOKEN)


def get_age(message):
    while True:
        try:
            age = int(message.text)
            flag = db_worker.new_user(user_id=message.from_user.id, age=age)
            if flag:
                bot.reply_to(message, "Спасибо! Ваш возраст сохранен", reply_markup=keyboards.start_keyboard)
            else:
                bot.reply_to(message, "Ваш возраст изменен", reply_markup=keyboards.default_keyboard)
            break

        except ValueError:
            bot.reply_to(message, "Введите число")


def build(chat_id, user_id, books_id=-1):
    temp = db_worker.parse_to_message(user_id, books_id=books_id)
    if temp:
        name, description, author, file = temp
        bot.send_photo(chat_id=chat_id, photo=open(f"covers/{file}.jpg", "rb"),
                       caption=f"{name}\nАвтор: {author}\nОписание: {description}")
        bot.send_document(chat_id=chat_id, document=open(f"books/{file}.fb2", "rb"))
    else:
        bot.send_message(chat_id=chat_id, text="На этом пока все, приходите позже")
