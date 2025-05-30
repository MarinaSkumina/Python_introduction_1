import psycopg2

# вывод только комнат
cur.execute('''
    with student_age as (
        select room_id, EXTRACT(year FROM AGE(current_date, birthday)) :: int as age
        from students
        )
    select room_name, 
           ROUND(AVG(age), 1) as avg_age
    from student_age inner join rooms as r using(room_id)
    group by room_name
    order by avg_age
    limit 5;
''')

# Getting the results of the query
version = cur.fetchall()[0]
print(version)