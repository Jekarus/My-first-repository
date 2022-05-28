import sqlite3
import menu2



def input_player():
    base_player = sqlite3.connect('data_users.db')  # база данных пользователей приложения
    cur = base_player.cursor()
    r = cur.execute('SELECT * FROM player').fetchall()  # считываем все данные с файла sqlite
    all_users = {}
    for row in r:
        # pl = row[0]
        # pas = row[1]
        all_users[row[0]] = row[1]
    print(all_users)
    user = input("Введите логин: ")
    if user in all_users:
        print("Привет ", user,)
        password = all_users.get(user)
        pas = input("Введите пароль: ")
        if password == pas:
            print("Успешный вход")
            menu2.menu_dop(user)
        else:
            print("Отказано")
    else:
        print("Пользователь отсутствует")