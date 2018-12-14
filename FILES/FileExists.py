# this program check whether the file exists or not
# we can also use the x mode for that but it will create the file if it doesn't exist and
# and if it exists it will show an error



import sys,os
if os.path.isfile("MULTIPLE STRINGS.txt"):


    file = open("MULTIPLE STRINGS.txt", "a")
    print("Enter the text (Type . when you are done) ")

    char = ''
    while char != '.':
        char = input()
        file.write(char + '\n')

    file.close()

else:
    print("FILE NOT FOUND ")
    sys.exit()




