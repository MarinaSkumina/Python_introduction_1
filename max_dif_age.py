import psycopg2

# вывод только комнат
cur.execute('''
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
	limit 10;
''')