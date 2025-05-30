import Query_to_json
import Query_to_xml

query_1 = '''
            SELECT rooms.room_id, rooms.room_name, COUNT(student_id)
            FROM students INNER JOIN rooms USING (room_id)
            GROUP BY rooms.room_name, rooms.room_id
            ORDER BY rooms.room_id
'''
query_xml = "SELECT query_to_xml('" + query_1 + "', true, false, '');"
query_json = 'SELECT json_agg(in_query) FROM (' + query_1 + ') as in_query;'
file_name = 'num_stud_in_rooms'

# Choosing the type of output file XML or JSON:
input_done = False
while input_done == False:
    print('Type output-file format (XML or JSON):')
    output_type = input()
    if output_type == 'XML':
        Query_to_xml.import_to_xml(query_body=query_xml, file_name=file_name)
        input_done = True
    elif output_type == 'JSON':
        Query_to_json.import_to_json(query_body=query_json, file_name=file_name)
        input_done = True
    else:
        print ('The type output-file format is incorrect')

