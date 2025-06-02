import psycopg2
from xml.etree import ElementTree as ET
from DB_connection import connection

@connection
def import_to_xml(conn, query_body: str, file_name: str) -> None:
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Querying the list of rooms with number of students in each
    file_name = file_name + '.xml'
    cur.execute(query_body)
    # Getting the results of the query
    data_xml = cur.fetchall()[0][0]
    print(data_xml)
    # Transforming string to xml-format
    tree = ET.XML(data_xml)
    # Writing data to xml-file
    with open(file_name, "wb") as f:
        f.write(ET.tostring(tree))
