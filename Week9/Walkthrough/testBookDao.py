from BookDAO import bookDao
#it calls it from the jaysus file name not the class you defined *in* the file
#you call python and the name of this file  on command line
#then check the sql command line separately to ensure the change was made
print ("this is a print out from testBookDao.py")

book = {
    'ISBN': 19456,
    'price': 12,
    'author': 'Octavia Butler',
    'title': 'some fantasy book'

}

book2 = {
    'ISBN': 1234567,
    'price': 999,
    'author': 'mary',
    'title': 'had a little lambchop'

}


#1.to check that create() works do this  returnValue = bookDao.create(book) 
#2. returnValue = result = bookDao.getAll()
#returnValue = bookDao.getAll()
#print(returnValue)
returnValue = bookDao.findById(book2['ISBN'])
print(returnValue)
print("*after findById*",(str(returnValue)))
returnValue = bookDao.update(book2)
print("*after update*",(str(returnValue)))
#returnValue = bookDao.delete(book2['ISBN'])

#print("*after delete*",(str(returnValue)))

returnValue = bookDao.getAll()
print("*final getAll*",(str(returnValue)))