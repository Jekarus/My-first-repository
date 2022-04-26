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
                Записная Книга 1.0
            1. Список
            2. Добавить аккаунт
            3. Изменить аккаунт
            4. Выход
            """
        )
        choice = input("Выберите пункт меню: ")
        print()
        if choice == '1':
            read_list1.read()
        if choice == '2':
            add_akk2.add()
        if choice == '3':
            file3.chak()
        if choice == '4':
            print("Завершение программы")
menu()

