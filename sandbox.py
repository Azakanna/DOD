password = 'пароль'
input_password = input('Пароль: ')

if input_password == password:
    print('Вы успешно авторизовались')
else:
    print('Пароль неверный!')











import hashlib

def  my_hash(text):
    return  hashlib.sha256(text.encode()).hexdigest()
password = 'пароль'
hash_password = '2dbc574daca52689a24fb60e835f8c19a36400830df7350859dd32d1abaaec5d'  #пароль
#print(my_hash(password))
# пароль - 2dbc574daca52689a24fb60e835f8c19a36400830df7350859dd32d1abaaec5d
input_password = input('Введите пароль: ')
hash_input_password = my_hash(input_password)

if hash_password == hash_input_password:
    print('Вы успешно авторизовались')
else:
    print('Пароль неверный!')
if input_password == password:
    print('Вы успешно авторизовались')
else:
    print('Пароль неверный!')










#########     ХЕШИРОВАНИЕ     ############

import  hashlib

def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

hash_password = '2dbc574daca52689a24fb60e835f8c19a36400830df7350859dd32d1abaaec5d'

input_password = input('Введите пароль: ')
hash_input_password = my_hash(input_password)

if hash_password == hash_input_password:
   print('Вы успешно авторизовались')
else:
    print('Пароль неверный!')

###########################################





























########### БАЗА ДАННЫХ  ##################

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               #(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Добавление данных
cursor.execute("INSERT INTO users (name, age) VALUES ('ЧЕЛИК 1', 18)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Челик 2', 20)")

# Получение данных
cursor.execute("SELECT * FROM users")
all_rows = cursor.fetchall()
for row in all_rows:
   print(row)

# Сохранение изменений/закрытие соединения
conn.commit()
conn.close()

############################################




######### РЕГИСТРАЦИЯ/АВТОРИЗАЦИЯ #############

# Программа для регистрации и авторизации пользователей

# Словарь для хранения зарегистрированных пользователей

registered_users = {}


def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    registered_users[username] = password
    print("Пользователь успешно зарегистрирован.")


def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if username in registered_users and registered_users[username] == password:
        pass
        #print("Вход выполнен успешно.")
    else:
        pass
        #print("Ошибка: неверное имя пользователя или пароль.")


# Основной код программы
while True:
    print("1. Зарегистрироваться")
    print("2. Войти")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Ошибка: некорректный выбор. Попробуйте еще раз.")
