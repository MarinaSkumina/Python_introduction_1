import Query_init

# Query body for choosing 'Five rooms with the highest age difference among students'
query_1 = '''
    with student_dif_age as (
        select room_name, 
	    (first_value(birthday) over w - last_value(birthday) over w) as dif_age
	    from students inner join rooms using(room_id)
	    window w as(
		partition by room_name 
	    order by (birthday) desc 
	    rows between unbounded preceding and unbounded following
	)
	)
	select room_name, ROUND(AVG(dif_age), 2) as dif_age
	from student_dif_age
	group by room_name
	order by dif_age desc
	limit 5
'''

file_name = '5_max_dif_age'

# Performing choosing type of output file format function
Query_init.query_init(query_body=query_1, file_name=file_name)

