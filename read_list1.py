import sqlite3

# добавление аккаунта

def read():
    base = sqlite3.connect('data_akk.db')
    cur = base.cursor()
    r = cur.execute('SELECT * FROM akk').fetchall() # считываем все данные с файла sqlite
    for row in r:   # отображение данных в меню
        print("Ид: ", row[0])   # считывание столбца
        print("Имя аккаунта: ", row[1])
        print("Логин: ", row[2])
        print("Пароль: ", row[3])
        print("--------------------------------")