from telebot import types

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
default_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
settings_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

start = types.KeyboardButton("Начать")
further = types.KeyboardButton("Далее")
settings = types.KeyboardButton("Настройки")
back = types.KeyboardButton("Назад")
change_age = types.KeyboardButton("Изменить возраст")
# change_rate = types.KeyboardButton("Изменить опыт")

start_keyboard.add(start)
default_keyboard.add(further, settings)
settings_keyboard.add(change_age, back)
