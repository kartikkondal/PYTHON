raza = True

file = open("DOCUMENT.TXT","r+")
while (raza == True):
    print("Write anything ")
    str1 = input("Write anything here ")
    file.write(str1+'\n')

    raza = input("Do you want to write anything else [y/n]")
    if raza=='n':
        raza = False
    else:
        raza = True

file.close()

