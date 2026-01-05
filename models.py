from database import get_db

def create_table():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    db.commit()

def add_task(title):
    db = get_db()
    db.execute("INSERT INTO tasks(title) VALUES(?)", (title,))
    db.commit()

def get_tasks():
    db = get_db()
    rows = db.execute("SELECT * FROM tasks").fetchall()
    return [dict(row) for row in rows]

def delete_task(task_id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    db.commit()
