# We are inserting a class object inside a data file(binary file ) we have no software to see it so we are going to make a program to read it too

# we imported a built-in module called PICKLE and a user-made module which is (student from student.py) which is created by us

#

import  pickle,student  #The student.py module which we created which has the student class defined in it



file = open("student.dat","wb")  #opened the object of the file

s = student.Student(123,'john',90)

pickle.dump(s,file)

file.close()
