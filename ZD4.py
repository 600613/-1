import sqlite3

#Создание базы данных и таблицы если такая еще не создана
#Operation - операция, KDVO - количество денег в операции, ItogS - итоговая сумма
def CreateDB():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS core_n (Id INTEGER PRIMARY KEY, Operation text, KDVO float,ItogS float)")
    con.commit()

#Функция добавления данных
def AddDB():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    A = input('Введите операцию ')
    B = float(input('Введите колличество денег в операции '))
    C = float(input('Введите итоговую сумму '))
    lid = cur.lastrowid
    data = [lid, A, B, C]
    cur.executemany("INSERT INTO core_n VALUES (?, ?, ?, ?)", (data,))
    con.commit()

#Функция вывода базы данных
def PrintDB():
    con = sqlite3.connect("database.db")
    with con:
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM core_n")

        for row in rows:
            print(row)

#Функция редактирования
def UpdateDB():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    while True:
        print("Какие данные изменить: \n 1.Оперяция \n 2.Количество денег в операции \n 3.Итоговая сумма \n")
        x = int(input())
        if x == 0:
            break
        elif x == 1:
            a1 = input("Под каким id изменить данные: ")
            b1 = input("На какое значение изменить: ")
            sql = "UPDATE core_n SET Operation = (?) WHERE id = (?)"
            cur.execute(sql, (b1, a1))
            break
        elif x == 2:
            a2 = input("Под каким id изменить данные ")
            b2 = input("На какое значение изменить ")
            sql = "UPDATE core_n SET KDVO = (?) WHERE id = (?)"
            cur.execute(sql, (b2, a2))
            break
        elif x == 3:
            a = input("Под каким id изменить данные ")
            b = input("На какое значение изменить ")
            sql = "UPDATE core_n SET ItogS = (?) WHERE id = (?)"
            cur.execute(sql, (b, a))
            break
        else:
            print('Некорректный ввод')
    con.commit()

#Функция удаления данных по id
def DeleteDB():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    a = input("Под каким id удалить данные ")
    cur.executemany("DELETE FROM core_n WHERE Id = (?)", a)
    cur.executemany("UPDATE core_n SET id = id - 1 WHERE id > (?)", a)
    con.commit()

CreateDB()
while True:
    print("Выберете действие: \n 0.Завершение программы \n 1.Добавление записи \n 2.Редактирование записи \n 3.Удаление записи \n 4.Просмотр таблицы")
    x  = int(input())
    if x == 0:
        break
    elif x == 1:
        AddDB()
    elif x == 2:
        UpdateDB()
    elif x == 3:
        DeleteDB()
    elif x == 4:
        PrintDB()
    else:
        print('Некорректный ввод')

    continue

