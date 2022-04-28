import sqlite3


# добавление аккаунта

def chak():
    cho = None
    while cho != '3':
        print(
            """
                xxxxxxxxxxxxxxxxxxxxxxxxxx
                x                        x
                x  Записная Книга v.1.1  x
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
            """ Изменение аккаунта по id"""
            base = sqlite3.connect('data_akk.db')
            cur = base.cursor()
            acc = input("Введите id аккаунта для изменения: ")
            log = input("Меняем логин на новый: ")
            pass_word = input("Введите новый пароль: ")
            update_login1 = 'UPDATE akk SET Login = ? WHERE id = ?;'    # меняем логин по иду
            update_login2 = 'UPDATE akk SET Password = ? WHERE id = ?;' # меняем пароль по иду
            cur.execute(update_login1, (log, acc))  # функция изменения логина
            cur.execute(update_login2, (pass_word, acc))    # функция изменения пароля
            print("Логин и пароль аккаунта изменен.")

            base.commit()
            cur.close()

            return 3    # Возврат 3 переменной cho, для выхода в основное меню

        elif cho == '2':
            """ Удаление аккаунта по id"""
            base = sqlite3.connect('data_akk.db')
            cur = base.cursor()

            acc = input("Введите id аккаунта для удаления: ")  # id аккаунта для удаления
            del_akk = 'DELETE FROM akk WHERE id =? '
            cur.execute(del_akk, acc)
            print("Аккаунт удален")

            base.commit()
            cur.close()

            return 3    # Возврат 3 переменной cho, для выхода в основное меню
        else:
            print("Нет такого меню!")
            print("Попробуй еще раз.")

