import mysql.connector
import config as config
#from mysql.connector import cursor

class BookDao:
    db = ""
#variable stores database connection,ok to leave blank
    def __init__(self):
        self.db = mysql.connector.connect(
        #    host = 'localhost',
        #    user= 'root',
        #    password = 'success',
        #    database ='datarepresentation'

 
        host=config.mysql['host'],
        user=config.mysql['username'],
        password=config.mysql['password'],
        database=config.mysql['database']
        )
        print ("connection @ __init__ made bookDAO.py")

#Create function
    def create(self, book):
        cursor = self.db.cursor()
        sql = "insert into books (ISBN, title, author, price) values (%s,%s,%s,%s)"
        values = [#denotes a list[]
            book['ISBN'],
            book['title'],
            book['author'],
            book['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid   
#Get All
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from books'
        cursor.execute(sql)
        results = cursor.fetchall()
        #this command will return tuples, below will convert to an array
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)#convert tuple into a Dict object
            returnArray.append(resultAsDict)
        return returnArray   
#Find
    def findById(self, ISBN):
        cursor = self.db.cursor()
        sql = 'select * from books where ISBN = %s'
        values = [ ISBN ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result) 
#Update        
    def update(self, book):
       cursor = self.db.cursor()
       sql = "update books set title = %s, author = %s, price = %s where ISBN = %s"
       #note on lines below you must change the order. It is important!
       values = [
           book['title'],
           book['author'],
           book['price'],
           book['ISBN']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return book
    
#Delete
    def delete(self, ISBN):
       cursor = self.db.cursor()
       sql = 'delete from books where ISBN = %s'
       values = [ISBN]
       cursor.execute(sql, values)
       
       return {}

#rather than convertToDict in each individual function, they can all call this one
    def convertToDict(self, result):
        colnames = ['ISBN','title', 'author', 'price']#extract the columns names as tuples and convert them too, they will appear on the printout
        book = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]#extract from the dict object
                book[colName] = value#make the item that matches the column name equal that value
        return book   

bookDao = BookDao()
#create a new instance of the class bookDao
#To create a new instance of a class in Python is choose a name for the object 
# and set it equal to the class name (that you created) followed by ().
#When referencing a class in Python, it should always be the class name with parenthesis ().
