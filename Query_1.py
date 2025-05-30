import Query_init

# Query body for choosing 'List of rooms and the number of students in each room'
query_1 = '''
            SELECT rooms.room_id, rooms.room_name, COUNT(student_id)
            FROM students INNER JOIN rooms USING (room_id)
            GROUP BY rooms.room_name, rooms.room_id
            ORDER BY rooms.room_id
'''

file_name = 'num_stud_in_rooms'

# Performing choosing type of output file format function
Query_init.query_init(query_body=query_1, file_name=file_name)


