import mysql.connector
#the code tells the computer to do the things your key strokes would otherwise
db=mysql.connector.connect(
  host="localhost",
  user="root",
  password="success",
  database="dataRepresentation")

cursor = db.cursor()
sql="select * from student where id = %s"
values=(1,)
cursor.execute(sql, values)
result=cursor.fetchall()
for x in result:
  print(x)