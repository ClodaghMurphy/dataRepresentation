import mysql.connector
#the code tells the computer to do the things your key strokes would otherwise
db=mysql.connector.connect(
  host="localhost",
  user="root",
  password="success",
  database="dataRepresentation")

cursor = db.cursor()
sql="insert into student(name,age) values(%s,%s)"
values=("Siobhan", 21)
cursor.execute(sql, values)
db.commit()
print("I just inserted one record for ya, ID:" ,cursor.lastrowid)