import sqlite3
from login_player import *

# добавление аккаунта

def add(user):
    base = sqlite3.connect(user + '.db')
    cur = base.cursor()
    web = input("Введите название аккаунта: ")
    while web == '':
        if web == '':
            print("Ошибка ввода")
            web = input("Введите название аккаунта: ")
        else:
            print("Название аккаунта принято")

    login = input("Введите логин аккаунта: ")
    while login == '':
        if login == '':
            print("Ошибка ввода")
            login = input("Введите логин аккаунта: ")
        else:
            print("Название логина принято")
    password = input("Введите пароль аккаунта: ")
    while password == '':
        if password == '':
            password = input("Введите пароль аккаунта: ")
            print("Ошибка ввода")
        else:
            print("Пароль принят")
        # NULL - не передаем значение столбу id, значение создается автоматически (Id INTEGER PRIMARY KEY)
    cur.execute("INSERT INTO akk VALUES(?, ?, ?);", (web, login, password))   # добавляем данные в БД

    base.commit()   # сохраняем бд


