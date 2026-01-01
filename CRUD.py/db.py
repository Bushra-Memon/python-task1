import sqlite3

def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id integer primary key autoincrement,
        name text not null,
        email text unique not null)
        """)

    user_data = [
        ('Bushra','bushra@gmail.com'),
        ('Fatima','fatima@gmail.com'),
        ('Alifa','alifa@gmail.com'),
        ('Muskan','muskan@gmail.com'),
        ('Mahenoor','mahenoor@gmail.com'),
        ('Vishakha','vishakha@gmail.com'),
        ('Hani','hani@gmail.com'),
        ('Moin','moin@gmail.com'),
        ('Fesal','fesal@gmail.com'),
        ('Faizan','faizan@gmail.com')
    ]

    #cursor.executemany('insert into user(name,email) values (?,?)', user_data)
    cursor.execute('insert into user(name,email) values (?,?)', ('saniya', 'saniya@gmail.com'))
    conn.commit()
    conn.close()
    print("Database,table created and data inserted successfully!")
create_db()