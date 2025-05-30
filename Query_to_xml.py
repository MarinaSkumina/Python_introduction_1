import psycopg2
from xml.etree import ElementTree as ET

#def import_to_xml(query_body: str, file_name: str) -> None:
    # Connect to postgres DB
conn = psycopg2.connect(dbname='students_rooms',
                        host="localhost",
                        user='postgres',
                        password='password',
                        port=5432)
# Open a cursor to perform database operations
cur = conn.cursor()
# Quering the list of rooms with number of students in each
query_body = '''
    SELECT query_to_xml('
        SELECT rooms.room_id, rooms.room_name, COUNT(student_id)
            FROM students INNER JOIN rooms USING (room_id)
            GROUP BY rooms.room_name, rooms.room_id
            ORDER BY rooms.room_id'
    , true, true, '');
'''
file_name = 'file_name' + '.xml'
cur.execute(query_body)
# Getting the results of the query
data_xml = cur.fetchall()[0][0]
print(data_xml)
# Transforming string to xml-format
root = ET.fromstring(data_xml)
tree = ET.ElementTree(root)
tree.write("pretty.xml")
with open("pretty.xml", 'r') as f:
    print(f.read())
#tree = ET.XML(data_xml)
# Writing data to xml-file
#with open(file_name, "wb") as f:
#    f.write(ET.tostring(tree))
# Closing the connection
cur.close()
conn.close()