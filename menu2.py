import sqlite3
import read_list1
import add_akk2
import change3
import add_text_file
from login_player import *

def menu_dop(user):
    base_player = sqlite3.connect(user + '.db')  # база данных пользователей приложения
    cur = base_player.cursor()

    base_player.execute("""CREATE TABLE IF NOT EXISTS player(
                                login TEXT,
                                password TEXT);             
                    """)
    base_player.commit()

    choice = None
    while choice != '5':
        print(
            """
                xxxxxxxxxxxxxxxxxxxxxxxxxx
                x                        x
                x  Записная Книга v.1.2  x
                x                        x
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            x                                x
            x         Меню:                  x
            x       1. Список                x
            x       2. Добавить аккаунт      x
            x       3. Изменить аккаунт      x
            x       4. Вывести в текс. файл  x
            x          данные аккаунта       x
            x       5. Выход                 x
            x                                x
            x                                x
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

            """
        )
        choice = input("Выберите пункт меню: ")
        print()
        if choice == '1':
            read_list1.read(user)
        if choice == '2':
            add_akk2.add(user)
        if choice == '3':
            change3.chak(user)
        if choice == '4':
            add_text_file.add_text(user)
        if choice == '5':
            print("Завершение программы")