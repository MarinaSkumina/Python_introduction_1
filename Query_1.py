import Query_init

# Query body for choosing 'List of rooms and the number of students in each room'
query_1 = '''
            SELECT r.room_id, r.room_name, COUNT(student_id)
            FROM students s 
                INNER JOIN rooms r ON s.room_id = r.room_id
            GROUP BY r.room_name, r.room_id
            ORDER BY r.room_id
'''

file_name = 'num_stud_in_rooms'

# Performing choosing type of output file format function
Query_init.query_init(query_body=query_1, file_name=file_name)