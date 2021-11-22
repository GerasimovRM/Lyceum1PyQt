import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()

cursor.execute("UPDATE films SET title='Нормальное название фильма' WHERE id=18004")
connection.commit()

import PyQt5.QtCore

print(PyQt5.QtCore.black)