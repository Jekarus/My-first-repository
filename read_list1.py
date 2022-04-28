import sqlite3

# добавление аккаунта

def read():
    base = sqlite3.connect('data_akk.db')
    cur = base.cursor()
    r = cur.execute('SELECT * FROM akk').fetchall() # считываем все данные с файла sqlite
    total = []  # список/счетчик количества аккаунтов
    for row in r:   # отображение данных в меню
        print("Ид: ", row[0])   # считывание столбца
        print("Имя аккаунта: ", row[1])
        print("Логин: ", row[2])
        print("Пароль: ", row[3])
        total.append(row[0])    # добавляем количество аккаунтов в список по id
        print("--------------------------------")

    print("Всего аккаунтов в базе: ", total[-1])