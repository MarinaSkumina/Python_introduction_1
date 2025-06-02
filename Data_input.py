import os.path
import json
from datetime import datetime

from DB_connection import connection

@connection
def path_input_rooms(conn) -> None:
    path_rooms = input("Please, enter the path to the rooms data file (push Enter for meaning by default):")
    if not path_rooms.strip():
        path_rooms = 'data/rooms.json'
    cur = conn.cursor()
    if os.path.exists(path_rooms):
        with open(path_rooms, encoding="UTF-8") as file_json:
            rooms = json.load(file_json)
        # Inserting information from json to table rooms through SQL-query
        for obj in rooms:
            # Check if the object is a dictionary
            if not isinstance(obj, dict):
                print(f"Skipping: object is not a dictionary → {obj}")
                continue
            # Check if required keys exist
            if 'id' not in obj or 'name' not in obj:
                print(f"Skipping: missing 'id' or 'name' keys → {obj}")
                continue

            # Check data types of values
            if not isinstance(obj['id'], int):
                print(f"Skipping: 'id' must be an int → {obj}")
                continue
            if not isinstance(obj['name'], str):
                print(f"Skipping: 'name' must be a string → {obj}")
                continue

            try:
                cur.execute(
                    "INSERT INTO rooms (room_id, room_name) VALUES (%s, %s)",
                    (obj['id'], obj['name'])
                )
            except Exception as e:
                print(f"Error inserting object {obj}: {e}")
            conn.commit()
    else:
        print("The path is incorrect or not exists")
    # Checking if data is saved
    cur.execute("select * from rooms limit 1;")
    # Getting the query result
    version = cur.fetchone()
    print(version)


path_input_rooms()

# Reading json file students.json
@connection
def path_input_students(conn) -> str:
    students_path = input("Please, enter the path to the students data file (push Enter for meaning by default):")
    if not students_path.strip():
        students_path = "data/students.json"
    cur = conn.cursor()
    if os.path.exists(students_path):
        with open(students_path, encoding="UTF-8") as file_json:
            students = json.load(file_json)
        # Inserting information from json to table students through SQL-query
        for obj in students:
            # Check if the object is a dictionary
            if not isinstance(obj,dict):
                print(f"Skipping: object is not a dictionary - {obj}")
                continue
            #Check if required keys exist
            for key in obj.keys():
                if key not in ['id', 'birthday', 'name', 'sex', 'room']:
                    print(f"Skipping: missing {key}")
                continue

            #Check data types of values
            if not isinstance(obj['id'], int):
                print(f"Skipping: 'id' must be an int - {obj}")
                continue
            if not isinstance(obj['birthday'], str):
                print(f"Skipping: 'birthday' must be a str - {obj}")
                continue
            if not isinstance(obj['name'], str):
                print(f"Skipping: 'name' must be a str - {obj}")
                continue
            if not isinstance(obj['sex'], str):
                print(f"Skipping: 'sex' must be a str - {obj}")
                continue
            if not isinstance(obj['room'], int):
                print(f"Skipping: 'room' must ber an int - {obj}")
                continue
            try:
                cur.execute(
                    "INSERT INTO students (student_id, birthday, student_name, sex, room_id) VALUES (%s, %s, %s, %s, %s)", \
                    (obj['id'], obj['birthday'], obj['name'], obj['sex'], obj['room'])
                )
            except Exception as e:
                print(f"Error inserting object {obj}: {e}")
            conn.commit()
    else:
        print("The path is incorrect or not exists")
    # Checking if data is saved
    cur.execute("select * from students limit 1;")
    # Getting query result
    version = cur.fetchone()
    print(version)


path_input_students()


