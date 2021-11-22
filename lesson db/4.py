import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()

id_field = input("Введите id: ")

cursor.execute(f"DELETE FROM films WHERE id={id_field}")
connection.commit()
