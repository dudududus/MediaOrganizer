import sqlite3

def init_db():
    conn = sqlite3.connect("media.db")
    c = conn.cursor()
    c.execute(''''
        CREATE TABLE IF NOT EXISTS media (
            id INTEGER PRIMARY KEY,
            filename TEXT,
            tags TEXT,
            description TEXT
        )
    '''')
    conn.commit()
    return conn

def insert_media(conn, filename, tags, description):
    c = conn.cursor()
    c.execute("INSERT INTO media (filename, tags, description) VALUES (?, ?, ?)",
              (filename, tags, description))
    conn.commit()
