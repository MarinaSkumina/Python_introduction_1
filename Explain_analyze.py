import psycopg2
import pprint

body_query_1 = '''
EXPLAIN ANALYZE SELECT rooms.room_id, rooms.room_name, COUNT(student_id)
        FROM students INNER JOIN rooms USING (room_id)
        GROUP BY rooms.room_name, rooms.room_id
        ORDER BY rooms.room_id;
'''

body_query_2 = '''
    EXPLAIN ANALYZE 
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
'''

body_query_3 = '''
    EXPLAIN ANALYZE
    with student_dif_age as (
        select room_name, 
	    (first_value(birthday) over w - last_value(birthday) over w) as dif_age
	    from students inner join rooms using(room_id)
	    window w as(
		partition by room_name 
	    order by (birthday) desc 
	    rows between unbounded preceding and unbounded following
	)
	order by dif_age
	)
	select room_name, ROUND(AVG(dif_age), 2) as dif_age
	from student_dif_age
	group by room_name
	order by dif_age desc
	limit 5;
'''

body_query_4 = '''
    EXPLAIN ANALYZE
    select room_name
    from students inner join rooms using (room_id)
    where sex = 'M'
    intersect 
    select room_name
    from students inner join rooms using (room_id)
    where sex = 'F';
'''

def explain_analyze (body_query : str, query_num : int) -> str:
    conn = psycopg2.connect(dbname='students_rooms',
                                host="localhost",
                                user='postgres',
                                password='password',
                                port=5432)
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Querying the list of rooms with number of students in each
    cur.execute(body_query)
    # Getting the results of the query
    explain_analyze = cur.fetchall()
    print(type(explain_analyze))
    print("Query plan")
    with open ('explain_analyse.txt', 'a') as f:
        f.write(f"Query plan {query_num}\n")
        f.writelines([f'{line}\n' for line in explain_analyze])

    pprint.pprint(explain_analyze)
    # Closing the connection
    cur.close()
    conn.close()
    return explain_analyze

explain_analyze(body_query_1, 1)
explain_analyze(body_query_2,2)
explain_analyze(body_query_3, 3)
explain_analyze(body_query_4, 4)