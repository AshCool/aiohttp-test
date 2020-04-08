import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="main_db"
)

mycursor = mydb.cursor()
print(type(mydb))
print(type(mycursor))

mycursor.execute("select * from user_info")

for item in mycursor:
    print(item)