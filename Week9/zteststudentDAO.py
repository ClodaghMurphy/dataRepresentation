from zstudentDAO import studentDAO
#create
latestid = studentDAO.create(('mark', 45))
# find by id
result = studentDAO.findByID(latestid);
print (result)
#update, pass in the tuple
studentDAO.update(('FriedlFriedl',21,latestid))
result = studentDAO.findByID(latestid);
print (result)
# get all
allStudents = studentDAO.getAll()
for student in allStudents:
 print(student)
# delete
studentDAO.delete(latestid)