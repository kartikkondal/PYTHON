
file = open("Demo","a")

Number1, Number2 = [int(x) for x in input("Enter two numbers ").split()]

try:
    c = Number1/Number2
    print(c)
    file.write('\nWriting %f into file ' %c)


except ZeroDivisionError:
    pass
else:
    print("You have entered a non zero number ")


finally:
    file.close()
    print("The file is closed ")


print("The code after Error ")

