import mysql.connector as connector
from learn_day015.ConnectionUtil import get_connection, close_connection

select_all = "Select * from Actor where actor_id = %s order by actor_id"
value = ('200',)

conn = get_connection()
cursor = conn.cursor()

cursor.execute(select_all, value)
result = cursor.fetchone()

print(result)

for eachRecord in result:
    print(type(eachRecord), eachRecord)


cursor.close()
close_connection(conn)
