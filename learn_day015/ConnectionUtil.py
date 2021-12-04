import mysql.connector as connector
# How to connect to Database
def get_connection():
    conn = connector.connect(
        host= 'localhost',
        port=3306,
        user = 'root',
        password='password',
        database='sakila'
    )
    return conn


def close_connection(conn):
    conn.commit()
    conn.close()