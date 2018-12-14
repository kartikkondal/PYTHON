# Assertion is used to give an error just like try and except block
# but the difference is that in try and except block the compiler is going to give an error for a particular situation but and if we did not added try and
# except block then it will generate an error and thus to continue the flow of the program we use try and except
# but in the case of Assertion we want to stop the working of the program at some input or at some condition
# the syntax is assert (condition for which the program should run smoothly ) (,) "the statement you want to print in the console "

#
# the code starts from here just comment(shift+/) out the piece of code that you want to display as output
# THE CODE STARTS FROM HERE-----
# number = int(input("Enter even number only "))
#
#
# assert number%2==0, "Don't fuck with me "
#
# print("&&&&&&")
# The above code will not print the &&&&&&& statement because it will give the error early so to contrinue the flow of the program so that it doesn't stop
# compiling we use assertion in try and catch block
# THE CODE ENDS HERE------------------------------------------
#

# # now lets put the code in try and catch block
try:
    num = int(input("enter the number "))

    assert num%2==0,"This is written ERROR of Assertion "

except AssertionError as object:
    print(object)



print("this is the code after the assertion ")

# now this is used when u want to continue the flow of the program along with Assertion
