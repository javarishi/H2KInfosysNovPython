import mysql.connector as connector
from learn_day015.ConnectionUtil import get_connection, close_connection

update_query = 'UPDATE actor SET first_name = %s,last_name = %s, last_update = CURRENT_TIMESTAMP WHERE actor_id = %s;'
values = ('ADAM', "AVIS", "225")

conn = get_connection()
cursor = conn.cursor()

cursor.execute(update_query, values)
# cursor.executemany(update_query, values)
print("Number of Rows affected " , cursor.rowcount)

cursor.close()
close_connection(conn)