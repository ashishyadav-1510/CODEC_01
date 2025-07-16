import sqlite3

# Create DB and table if not exists
def init_db():
    conn = sqlite3.connect("chatlog.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chatlog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Insert interaction into the database
def log_interaction(user_input, bot_response):
    conn = sqlite3.connect("chatlog.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chatlog (user_input, bot_response) VALUES (?, ?)",
                   (user_input, bot_response))
    conn.commit()
    conn.close()

# Initialize database when the module is imported
init_db()
