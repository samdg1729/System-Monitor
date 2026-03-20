import sqlite3

DB_NAME = "sysmon.db"

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS system_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        cpu_usage REAL,
        memory_used INTEGER,
        memory_total INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_stats(cpu, mem_used, mem_total):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO system_stats (cpu_usage, memory_used, memory_total)
    VALUES (?, ?, ?)
    """, (cpu, mem_used, mem_total))

    conn.commit()
    conn.close()

def fetch_history(limit=10):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT timestamp, cpu_usage, memory_used, memory_total
    FROM system_stats
    ORDER BY timestamp DESC
    LIMIT ?
    """, (limit,))

    rows = cur.fetchall()
    conn.close()
    return rows