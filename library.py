import telebot
import db_worker
import features
from config import *

bot = telebot.TeleBot(TOKEN)


def get_authors():
    connection, cursor = db_worker.connect()
    cursor.execute('SELECT DISTINCT author FROM books')
    authors = [row[0] for row in cursor.fetchall()]
    return authors


def get_inline_keyboard():
    authors = get_authors()
    button = [telebot.types.InlineKeyboardButton(
            text=author, callback_data=f'show_books_{author}')
            for author in authors]
    keyboard = [button[i:i + 3] for i in range(0, len(button), 3)]
    return telebot.types.InlineKeyboardMarkup(keyboard)



def get_books_inline_keyboard(author):
    connection, cursor = db_worker.connect()
    cursor.execute('SELECT name FROM books WHERE author=?', (author,))
    books = cursor.fetchall()
    button = [telebot.types.InlineKeyboardButton(
            text=book[0], callback_data=f'show_book_{book[0]}')
            for book in books]
    keyboard = [button[i:i + 2] for i in range(0, len(button), 2)]
    return telebot.types.InlineKeyboardMarkup(keyboard)


def show_books(call):
    author = call.data.split('_')[-1]
    keyboard = get_books_inline_keyboard(author)
    bot.send_message(call.message.chat.id, f'Книги автора {author}:',
                     reply_markup=keyboard)


def show_book(call):
    connection, cursor = db_worker.connect()
    books_id = cursor.execute('SELECT id FROM books WHERE name=?',
                              (call.data.split('_')[-1],)).fetchone()
    features.build(call.message.chat.id, call.message.from_user.id,
                   books_id=books_id[0])
