import sqlite3
import random


def connect():
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    return connection, cursor


def book_done(user_id: int, book_id: int):
    connection, cursor = connect()
    pk_id = cursor.execute("select id from users where user_id = " + str(user_id)).fetchone()
    cursor.execute("INSERT INTO user_books (user_id, book_id) VALUES (?, ?)",
                   (str(pk_id[0]), str(book_id)))
    connection.commit()
    connection.close()


def new_user(user_id: int, age: int):
    flag = False
    connection, cursor = connect()
    qnt = cursor.execute("select count(*) from users where user_id = ?", [str(user_id)]).fetchone()
    if qnt[0] == 0:
        cursor.execute('INSERT INTO users (user_id, age) VALUES (?, ?)',
                       (user_id, age))
        flag = True
    else:
        cursor.execute('update users set age = ? where user_id = ?', (age, user_id))
    connection.commit()
    connection.close()
    return flag


def parse_to_message(u_id):
    books_id = select_new_book(u_id)
    if books_id == -1:
        return 0
    else:
        connection, cursor = connect()
        res = cursor.execute("select name, description, author, file_name from books where id = ?", str(books_id))
        name, description, author, file = res.fetchone()
        connection.commit()
        connection.close()
        return name, description, author, file


def select_new_book(u_id):
    connection, cursor = connect()
    pk_id, age = cursor.execute("select id, age from users where user_id = ?", [str(u_id)]).fetchone()
    res = cursor.execute("select id from books where age_limit <= ?", [str(age)]).fetchall()
    res_u = cursor.execute("select book_id from user_books where user_id = ?", str(pk_id)).fetchall()
    connection.commit()
    connection.close()

    for i in range(len(res)):
        res[i] = list(res[i])[0]

    for i in range(len(res_u)):
        res_u[i] = list(res_u[i])[0]

    non_read = list(set(res) - set(res_u))
    if non_read:
        book_id = random.choice(non_read)
        book_done(u_id, book_id)
        return book_id
    else:
        return -1


