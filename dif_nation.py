import Query_init

# Query body for choosing 'List of rooms where students of different nationalities live'
query_1 = '''
    select room_name
    from students inner join rooms using (room_id)
    where sex = 'M'
    intersect 
    select room_name
    from students inner join rooms using (room_id)
    where sex = 'F'
'''

file_name = 'rooms_dif_nation'

# Performing choosing type of output file format function
Query_init.query_init(query_body=query_1, file_name=file_name)

