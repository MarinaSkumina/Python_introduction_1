import psycopg2


cur.execute('''
    select room_name
    from students inner join rooms using (room_id)
    where sex = 'M'
    intersect 
    select room_name
    from students inner join rooms using (room_id)
    where sex = 'F';
''')