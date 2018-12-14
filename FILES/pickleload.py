# This is used to read the binary file



import pickle

file = open("student.dat","rb")

obj = pickle.load(file)

obj.display()

file.close()