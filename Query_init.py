import Query_to_json
import Query_to_xml

# Choosing the type of output file XML or JSON:
def query_init (query_body : str, file_name : str) -> None:
    query_clean_xml = query_body.replace("'", "''").replace("\n", " ")
    query_xml = f"SELECT query_to_xml('{query_clean_xml}', true, false, '');"
    query_json = 'SELECT json_agg(in_query) FROM (' + query_body + ') as in_query;'
    input_done = False
    while input_done == False:
        output_type = (input('Type output-file format (XML or JSON), press Enter to choose JSON by default:')).lower()
        if not output_type.strip():
            output_type = "json"
        if output_type == 'xml':
            Query_to_xml.import_to_xml(query_body=query_xml, file_name=file_name)
            input_done = True
        elif output_type == 'json':
            Query_to_json.import_to_json(query_body=query_json, file_name=file_name)
            input_done = True
        else:
            print ('The type of output-file format is incorrect')
