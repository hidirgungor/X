import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "XXXX",
    database = "mydatabase"
)

mycursor = mydb.cursor()
# mycursor.execute("Create database mydatabase")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

print(mydb) 