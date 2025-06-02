import Query_init

# Query body for choosing 'Five rooms with the lowest average student age.'
query_1 = '''
      select room_name, 
           ROUND(AVG(EXTRACT(year FROM AGE(current_date, birthday)) :: int ), 1) as avg_age
    from students s 
        inner join rooms as r ON s.room_id = r.room_id
    group by room_name
    order by avg_age
    limit 5
'''

file_name = '5_min_avg_age'

# Performing choosing type of output file format function
Query_init.query_init(query_body=query_1, file_name=file_name)

