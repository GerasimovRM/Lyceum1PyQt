import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
template = input("Введите поле: ")
result = cursor.execute(f"""
SELECT {template} FROM films""").fetchall()

print(result)

# SELECT 'id' FROM films