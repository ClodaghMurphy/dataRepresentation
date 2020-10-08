import csv

#create a w=writeable csv file with this name in this directory
employee_file = open('employee_file.csv', mode='w') 

employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers, what', 'IT', 'March'])

employee_file.close()
#then check has it worked by inputting ls in the cmd - you can see a new csv file created, wow.
#cat employee_file.csv on the command line
#The cat command is used to concatenate files and print on the standard output.