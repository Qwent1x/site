import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()
cursor.execute('''SELECT * FROM artists''')
# Запитання 1. Інформація про скількох художників представлена у базі даних?
data = cursor.fetchall()

cursor.execute('''SELECT * FROM artists WHERE Gender == "Female"''')
# Запитання 2. Скільки жінок (Female) у базі?
data = cursor.fetchall()

cursor.execute('''SELECT * FROM artists WHERE "Birth Year" < 1900''')
data = cursor.fetchall()
# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
cursor.execute('''SELECT * FROM artists ORDER BY "Birth Year"''')

data = cursor.fetchall()

# Запитання 4*. Як звати найстаршого художника?
print(data[0])

conn.commit()
