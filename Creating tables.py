import os.path
import json
import psycopg2

# Connect to postgres DB
conn = psycopg2.connect(dbname='students_rooms',
                        host="localhost",
                        user='postgres',
                        password='password',
                        port=5432)
# Open a cursor to perform database operations
cur = conn.cursor()

# Drop table rooms if exists
cur.execute('''DROP TABLE IF EXISTS rooms CASCADE''')

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

# Reading json file rooms.json
def path_input_rooms () -> None:
    #print("Please, enter the path to the rooms data file")
    #path_rooms = input()
    path_rooms = "./rooms.json"
    if os.path.exists(path_rooms):
        with open(path_rooms, encoding="UTF-8") as file_json:
            rooms = json.load(file_json)
        # Inserting information from json to table rooms through SQL-query
        for obj in rooms:
            cur.execute(
                "INSERT INTO rooms (room_id, room_name) VALUES (%s, %s)", (obj['id'], obj['name'])
            )
        conn.commit()
        print(path_rooms)
    else:
        print("The path is incorrect or not exists")
        path_input_rooms ()


path_input_rooms()

# Checking if data is saved
cur.execute("select * from rooms limit 1;")

# Getting the query result
version = cur.fetchone()
print(version)

# Open a cursor to perform database operations
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS students''')

# Creating table students through SQL-query
cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
	student_id INTEGER PRIMARY KEY,
	birthday date,
	student_name text,
	sex text,
	room_id integer references rooms (room_id)
	);
	CREATE INDEX index_sex ON students USING HASH (sex);
''')
print("Table students created successfully")
conn.commit()

# Reading json file students.json
def path_input_students () -> str:
    #print("Please, enter the path to the students data file")
    #students_path = input()
    students_path = "./students.json"
    if os.path.exists(students_path):
        with open(students_path, encoding="UTF-8") as file_json:
            students = json.load(file_json)
        # Inserting information from json to table students through SQL-query
        for obj in students:
            cur.execute(
                "INSERT INTO students (student_id, birthday, student_name, sex, room_id) VALUES (%s, %s, %s, %s, %s)", \
                (obj['id'], obj['birthday'], obj['name'], obj['sex'], obj['room'])
            )
            conn.commit()
    else:
        print("The path is incorrect or not exists")
        path_input_students()


path_input_students()

# Checking if data is saved
cur.execute("select * from students limit 1;")

# Getting query result
version = cur.fetchone()
print(version)

# Closing the connection
cur.close()
conn.close()