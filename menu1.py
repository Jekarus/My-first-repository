import sqlite3
import reg_player
import login_player

""" Приложение Записная книжка 1.0  """
def player_base():

    base_player = sqlite3.connect('data_users.db')  # база данных пользователей приложения
    cur_base_player = base_player.cursor()

    base_player.execute("""CREATE TABLE IF NOT EXISTS player(
                            login TEXT,
                            password TEXT);             
                """)
    base_player.commit()


def main():
    player_base()
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
            x         Добро Пожаловать!      x
            x                                x
            x       1. Регистрация           x
            x       2. Войти                 x
            x       3. Закрыть программу     x
            x                                x
            x                                x 
            x                                x            
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            
            """
        )
        cho = input("Выберите пункт меню: ")
        print()
        if cho == '1':
            reg_player.registration()
        elif cho == '2':
            login_player.input_player()
        else:
            print("Нет такого меню")

main()
