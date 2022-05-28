import sqlite3
from login_player import *

# добавление аккаунта

def chak(user):
    cho = None
    while cho != '3':
        print(
            """
                xxxxxxxxxxxxxxxxxxxxxxxxxx
                x                        x
                x  Записная Книга v.1.2  x
                x                        x
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            x                                x
            x     Меню: Изменить аккаунт     x
            x  1. Изм. логин и пароль акк.   x
            x  2. Удалить акк.               x
            x  3. Вернуться в пред. меню     x
            x                                x 
            x                                x
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            """
        )
        cho = input("Выберите пункт меню: ")

        if cho == '1':
            """ Изменение аккаунта по имени"""
            base = sqlite3.connect(user + '.db')
            cur = base.cursor()
            r = cur.execute('SELECT * FROM akk').fetchall()  # считываем все данные с файла sqlite
            acc = input("Введите имя аккаунта для изменения: ")
            r = cur.execute('SELECT * FROM akk').fetchall()  # считываем все данные с файла sqlite
            all_akk = []
            for row in r:
                all_akk.append(row[0])
            for i in all_akk:
                if acc == i:
                        print("Имя найдено")
                        log = input("Меняем логин на новый: ")
                        update_login = 'UPDATE akk SET Login = ? WHERE WebSite = ?;'  # меняем логин по имени аккаунта
                        cur.execute(update_login, (log, acc))  # функция изменения логина
                        pass_word = input("Введите новый пароль: ")
                        update_pas = 'UPDATE akk SET Password = ? WHERE WebSite = ?;'  # меняем пароль по имени
                        cur.execute(update_pas, (pass_word, acc))  # функция изменения пароля
                else:
                        print("Такого имени не существует")
            print("Данные изменены")
            base.commit()
            cur.close()

            return 3    # Возврат 3 переменной cho, для выхода в основное меню

        elif cho == '2':
            """ Удаление аккаунта по имени"""
            base = sqlite3.connect(user + '.db')
            cur = base.cursor()

            acc = input("Введите название аккаунта для удаления: ")  # id аккаунта для удаления
            del_akk = 'DELETE FROM akk WHERE WebSite =?;'
            cur.execute(del_akk, (acc,))    # acc пишется в формате кортежа, поэтому ставим запятую
            print("Аккаунт удален")

            base.commit()
            cur.close()

            return 3    # Возврат 3 переменной cho, для выхода в основное меню
        else:
            print("Нет такого меню!")
            print("Попробуй еще раз.")

