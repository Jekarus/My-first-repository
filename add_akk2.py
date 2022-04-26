import sqlite3


# добавление аккаунта

def add():
    base = sqlite3.connect('data_akk.db')
    cur = base.cursor()

    web = input("Введите название аккаунта: ")
    login = input("Введите логин аккаунта: ")
    password = input("Введите пароль аккаунта: ")
    # NULL - не передаем значение столбу id, значение создается автоматически (Id INTEGER PRIMARY KEY)
    cur.execute("INSERT INTO akk VALUES(NULL, ?, ?, ?);", (web, login, password))   # добавляем данные в БД

    base.commit()   # сохраняем бд
