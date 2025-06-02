from DB_connection import connection

@connection
def create_tables(conn):
    cur = conn.cursor()
    # Creating table rooms through SQL-query
    cur.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
        room_id integer primary key,
        room_name text
        );
        CREATE INDEX index_room_id ON rooms (room_id);
    ''')
    print("Table rooms created successfully")
    conn.commit()
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Creating table students through SQL-query
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        birthday date,
        student_name text,
        sex text,
        room_id integer references rooms (room_id) ON DELETE CASCADE
        );
        CREATE INDEX index_sex ON students USING HASH (sex);
    ''')
    print("Table students created successfully")
    conn.commit()


create_tables()