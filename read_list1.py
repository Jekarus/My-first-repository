import sqlite3
from login_player import *


def read(user):
    base = sqlite3.connect(user + '.db')
    cur = base.cursor()
    r = cur.execute('SELECT * FROM akk').fetchall()     # считываем все данные с файла sqlite
    total = 1
    for row in r:   # отображение данных в меню
        print("Аккаунт №:", total)
        print("Имя аккаунта: ", row[0])
        print("Логин: ", row[1])
        print("Пароль: ", row[2])
        total += 1
        print("--------------------------------")
    print("Всего аккаунтов в базе: ", total - 1)


