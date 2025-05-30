import json
from pprint import pprint

with open("rooms.json", encoding="UTF-8") as file_in:
    rooms = json.load(file_in)
pprint(rooms[0])

with open("students.json", encoding="UTF-8") as file_in:
    students = json.load(file_in)
pprint(students[0])
