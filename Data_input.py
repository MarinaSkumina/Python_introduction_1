import os.path
import json
from DB_connection import connection

@connection
def path_input_rooms(conn) -> None:
    path_rooms = input("Please, enter the path to the rooms data file (push Enter for meaning by default:)")
    if not path_rooms.strip():
        path_rooms = 'data/rooms.json'
    cur = conn.cursor()
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
    # Checking if data is saved
    cur.execute("select * from rooms limit 1;")
    # Getting the query result
    version = cur.fetchone()
    print(version)


path_input_rooms()

# Reading json file students.json
@connection
def path_input_students(conn) -> str:
    students_path = input("Please, enter the path to the students data file (push Enter for meaning by default:)")
    if not students_path.strip():
        students_path = "data/students.json"
    cur = conn.cursor()
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
    # Checking if data is saved
    cur.execute("select * from students limit 1;")
    # Getting query result
    version = cur.fetchone()
    print(version)


path_input_students()


