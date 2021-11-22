import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
id_field = input("Введите id: ")
title = input("Введите название: ")
year = input("Введите год: ")
genre_id = input("Введите id жанра: ")
duration = input("Введите продолжительность: ")
query = f"""INSERT INTO films(id, title, year, genre, duration) VALUES ({id_field}, {title}, {year}, {genre_id}, {duration})"""
print(query)
try:
    cursor.execute(query, [id_field, title, year, genre_id, duration])
except sqlite3.OperationalError as e:
    print("Что-то пошло не так:", e)
connection.commit()