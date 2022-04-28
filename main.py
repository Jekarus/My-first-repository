import sqlite3
import read_list1
import add_akk2
import file3

""" Приложение Записная книжка 1.0  """

def data_base():
    """
    База данных аккаунтов
    :return:
    """
    base = sqlite3.connect('data_akk.db')   # создали базу данных
    cur = base.cursor()     # подключились для редактирования

    base.execute("""CREATE TABLE IF NOT EXISTS akk(
                Id INTEGER PRIMARY KEY,
                WebSite TEXT,
                Login TEXT,
                Password TEXT);               
    """)
    base.commit()


def menu():
    base = sqlite3.connect('data_akk.db')  # создали базу данных
    cur = base.cursor()  # подключились для редактирования
    data_base()
    choice = None
    while choice != '4':
        print(
            """
                xxxxxxxxxxxxxxxxxxxxxxxxxx
                x                        x
                x  Записная Книга v.1.1  x
                x                        x
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            x                                x
            x         Меню:                  x
            x       1. Список                x
            x       2. Добавить аккаунт      x
            x       3. Изменить аккаунт      x
            x       4. Выход                 x
            x                                x 
            x                                x
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            
            """
        )
        choice = input("Выберите пункт меню: ")
        print()
        if choice == '1':
            read_list1.read()
        elif choice == '2':
            add_akk2.add()
        elif choice == '3':
            file3.chak()
        elif choice == '4':
            print("Завершение программы")
        else:
            print("Нет такого меню!")
menu()

