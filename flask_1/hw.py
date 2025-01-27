from flask import Flask, session
import random
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Для сессий

# Глобальные переменные
CARS = ["Chevrolet", "Renault", "Ford", "Lada"]
CATS = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt")

# Предварительная загрузка текста книги
with open(BOOK_FILE, "r", encoding="utf-8") as book:
    WORDS = [word.strip(",.?!:;") for word in book.read().split() if word.strip(",.?!:;")]


# Задача 1: /hello_world
@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"


# Задача 2: /cars
@app.route("/cars")
def cars():
    return ", ".join(CARS)


# Задача 3: /cats
@app.route("/cats")
def cats():
    return f"Случайная порода кошки: {random.choice(CATS)}"


# Задача 4: /get_time/now
@app.route("/get_time/now")
def get_time_now():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Точное время: {current_time}"


# Задача 5: /get_time/future
@app.route("/get_time/future")
def get_time_future():
    future_time = (datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")
    return f"Точное время через час будет: {future_time}"


# Задача 6: /get_random_word
@app.route("/get_random_word")
def get_random_word():
    return f"Случайное слово: {random.choice(WORDS)}"


# Задача 7: /counter
@app.route("/counter")
def counter():
    if "visits" not in session:
        session["visits"] = 0
    session["visits"] += 1
    return f"Эта страница была открыта {session['visits']} раз."


if __name__ == "__main__":
    app.run(debug=True)