import sqlite3
import hashlib

# Подключение к базе данных
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы для хранения пользователей
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# Регистрация нового пользователя
def register_user(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("Пользователь успешно зарегистрирован")

# НЕ РАБОЧАЯ АВТОРИЗАЦИЯ БЛЯТЬ
def login_user(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = cursor.fetchone()
    if user:
        print("Авторизация успешна")
    else:
        print("Неверное имя пользователя или пароль")

# Тут короче  где написано не дублируется это логин я его вручную менял для бд   а Гамлет пороль который выше уже через
# мд5 сделан в хеш
register_user('Не дублируется', 'Гамлет')

# Тут должно было быть авторизация но тоже нихуя не работет
login_user('Гамлет', 'Кирилл')

# Сохранение изменений / закрытие соединения
conn.commit()
conn.close()