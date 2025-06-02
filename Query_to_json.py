import json
import psycopg2
from DB_connection import connection

@connection
def import_to_json(conn, query_body: str, file_name: str) -> None:
    cur = conn.cursor()
    # Making query
    cur.execute(query_body)
    # Getting the results of the query
    version = cur.fetchone()[0]
    print(version)
    # Writting the results to json-file
    file_name = file_name + '.json'
    with open(file_name, 'w') as f:
        json.dump(version, f, indent=4)
        f.close()




