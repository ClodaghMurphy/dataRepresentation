import mysql.connector

db=mysql.connector.connect(
  host="localhost",
  user="root",
  password="success")

cursor = db.cursor()
cursor.execute("CREATE DATABASE dataRepresentation")