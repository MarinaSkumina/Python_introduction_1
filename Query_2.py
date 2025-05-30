import Query_init

# Query body for choosing 'Five rooms with the lowest average student age.'
query_1 = '''
    with student_age as (
        select room_id, EXTRACT(year FROM AGE(current_date, birthday)) :: int as age
        from students
        )
    select room_name, 
           ROUND(AVG(age), 1) as avg_age
    from student_age inner join rooms as r using(room_id)
    group by room_name
    order by avg_age
    limit 5
'''

file_name = '5_min_avg_age'

# Performing choosing type of output file format function
Query_init.query_init(query_body=query_1, file_name=file_name)

