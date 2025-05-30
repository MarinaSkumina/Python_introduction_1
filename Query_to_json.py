import json
import psycopg2

def import_to_json(query_body: str, file_name: str) -> None:
    # Connect to postgres DB
    conn = psycopg2.connect(dbname='students_rooms',
                            host="localhost",
                            user='postgres',
                            password='password',
                            port=5432)
    # Open a cursor to perform database operations
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
    # Closing the connection
    cur.close()
    conn.close()



