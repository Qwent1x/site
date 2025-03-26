import sqlite3

def create_table():
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS quiz(id INTEGER PRIMARY KEY AUTOINCREMENT, level TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS question(id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, wrong1 TEXT,
                wrong2 teXT, wrong3 TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS quiz_content(id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, quiz_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id)
                FOREIGN KEY (question) REFERENCES questions (id))''')
    conn.commit()

def fill_question():
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS quiz(id INTEGER PRIMARY KEY AUTOINCREMENT, level TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS question(id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, wrong1 TEXT,
                wrong2 teXT, wrong3 TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS quiz_content(id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, quiz_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id)
                FOREIG2N KEY (question) REFERENCES questions (id))''')
    n = input("Введіть кількість запитань: ")
    for i in range(int(n)):
        question = input(f"Введіть питання під номером {i}: ")
        answer = input(f"Введіть правильну відповідь: ")
        wrong_1 = input(f"Введіть першу не правильну відповідь: ")
        wrong_2 = input(f"Введіть другу не правильну відповідь: ")
        wrong_3 = input(f"Введіть третю не правильну відповідь: ")
        cur.execute('''INSERT INTO questions (question, answer, wrong_answer_1, wrong_answer_2, wrong_answer_3) VALUES (?,?,?,?,?)''', [question, answer, wrong_1, wrong_2, wrong_3])
        conn.commit()
    conn.close()
create_table()
fill_question()
