from telebot import types

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
default_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
settings_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

keyboard = types.InlineKeyboardMarkup(row_width=2)
add = types.InlineKeyboardButton(text="Принять ✅")
keyboard.add(add)

start = types.KeyboardButton("Начать")
further = types.KeyboardButton("Далее")
settings = types.KeyboardButton("Настройки")
back = types.KeyboardButton("Назад")
library = types.KeyboardButton("Показать библиотеку")
change_age = types.KeyboardButton("Изменить возраст")
# change_rate = types.KeyboardButton("Изменить опыт")

start_keyboard.add(start)
default_keyboard.add(further, library, settings)
settings_keyboard.add(change_age, back)
