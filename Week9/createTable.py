import mysql.connector
#the code tells the computer to do the things your key strokes would otherwise
db=mysql.connector.connect(
  host="localhost",
  user="root",
  password="success",
  database="dataRepresentation")

cursor = db.cursor()
sql="CREATE TABLE student2(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
cursor.execute(sql)