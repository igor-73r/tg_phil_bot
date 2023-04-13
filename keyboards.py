from telebot import types

default_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
settings_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
auto_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

further = types.KeyboardButton("Далее➡️")
settings = types.KeyboardButton("Настройки⚙️")
back = types.KeyboardButton("На главную⬅️")
library = types.KeyboardButton("Показать библиотеку📚📚")
change_age = types.KeyboardButton("Изменить возраст✏️")
auto = types.KeyboardButton("Авто❇️")
# change_rate = types.KeyboardButton("Изменить опыт")

default_keyboard.row(auto, library).row(settings)
settings_keyboard.row(change_age).row(back)
auto_keyboard.row(further).row(back)


def url_button(url):
    return types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="Скачать🌐", url=url)]])
