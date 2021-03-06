import mysql.connector
class StudentDAO:
    db=""#blank at the moment
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="success",
        database="datarepresentation"
 )#normally would come from a separate configuration file

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        #returnArray = []
        #for result in results:
        #    returnArray.append(self.converttoDictionary(result))
        return result

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from student where id = %s"
        values = (id,)#make a tuple with the id
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
        #return self.converttoDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update student set name= %s, age=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from student where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
    
   

studentDAO = StudentDAO()
#create a new instance