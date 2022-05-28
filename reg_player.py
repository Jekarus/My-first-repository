import sqlite3



def registration():
    base_player = sqlite3.connect('data_users.db')  # создали базу данных
    cur_base_player = base_player.cursor()  # подключились для редактирования
    log = input("Введите логин нового аккаунта: ")
    while log == '':
        if log == '':
            print("Ошибка ввода")
            log = input("Введите логин нового аккаунта: ")
        else:
            print("Логин принят")
    password = input("Введите пароль нового аккаунта: ")
    while password == '':
        if password == '':
            print("Ошибка ввода")
            password = input("Введите пароль нового аккаунта: ")
        else:
            print("Ок")
    password2 = input("Подтвердите пароль нового аккаунта: ")
    while password2 == '':
        if password2 == password:
            print("Пароль установлен")
        else:
            print("Пароль не совпадает")
            password2 = input("Подтвердите пароль нового аккаунта: ")
    print("Аккаунт добавлен.")
    cur_base_player.execute("INSERT INTO player VALUES(?, ?);", (log, password2))  # добавляем данные в БД
    base_player.commit()
    data_new_base(log)


def data_new_base(log):
    """
    База данных зареганного аккаунта
    :return:
    """
    base = log + '.db'
    base = sqlite3.connect(base)   # создали базу данных
    cur = base.cursor()     # подключились для редактирования

    base.execute("""CREATE TABLE IF NOT EXISTS akk(
                WebSite TEXT,
                Login TEXT,
                Password TEXT);               
    """)
    base.commit()