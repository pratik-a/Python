import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="student")

mycursor = mydb.cursor()

mycursor.execute("select * from sinfo")
result = mycursor.fetchall()

for i in result:
    print(i)