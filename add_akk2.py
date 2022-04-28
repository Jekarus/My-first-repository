import sqlite3


# добавление аккаунта

def add():
    base = sqlite3.connect('data_akk.db')
    cur = base.cursor()
    web = ''
    login = ''
    password = ''
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
        # NULL - не передаем значение столбу id, значение создается автоматически (Id INTEGER PRIMARY KEY)
    cur.execute("INSERT INTO akk VALUES(NULL, ?, ?, ?);", (web, login, password))   # добавляем данные в БД

    base.commit()   # сохраняем бд


