from DB_connection import connection

@connection
def truncate_tables(conn):
    cur = conn.cursor()
    # Truncate tables rooms and students
    cur.execute('''TRUNCATE TABLE rooms CASCADE''')
    cur.execute('''TRUNCATE TABLE students''')
    conn.commit()
    print(f"Tables rooms and students are truncated successfully")


truncate_tables()

