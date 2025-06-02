import psycopg2

def connection(func):
    def wrapper(*args, **kwargs):
        # Connect to postgres DB
        try:
            conn = psycopg2.connect(dbname='students_rooms',
                                     host="localhost",
                                     user='postgres',
                                     password='password',
                                     port=5432)
            result = func(conn, *args, **kwargs)
            conn.close()
            return result
        except Exception as e:
            # DB connection error
            print(f"The error has occurred. Details: {e}")
    return wrapper