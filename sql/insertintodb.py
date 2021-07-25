import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="student")

mycursor = mydb.cursor()

mycursor.execute("insert into sinfo values(\"pa\",\"kv\")")
mycursor.execute("select * from sinfo")

for i in mycursor:
    print(i)