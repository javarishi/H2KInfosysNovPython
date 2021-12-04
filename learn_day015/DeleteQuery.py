import mysql.connector as connector

myDB = connector.connect(
    host= 'localhost',
    port=3306,
    user = 'root',
    password='password',
    database='sakila'
)

mycursor = myDB.cursor()

print(myDB)
print(mycursor)

mycursor.close()
myDB.close()
