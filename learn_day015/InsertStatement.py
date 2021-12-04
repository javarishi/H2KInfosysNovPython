import mysql.connector as connector
from learn_day015.ConnectionUtil import get_connection, close_connection

insert_query = "INSERT INTO actor (first_name, last_name, last_update) VALUES ( %s, %s , CURRENT_TIMESTAMP)"
# values = ('KRISHAN', 'YADAV')
values = [('Balram', "YADAV"), ('Pradyumn', "YADAV"), ('Devon', "Dice") ,]
conn = get_connection()
cursor = conn.cursor()

# cursor.execute(insert_query, values)
cursor.executemany(insert_query, values)
print("Number of Rows affected " , cursor.rowcount)

cursor.close()
close_connection(conn)





