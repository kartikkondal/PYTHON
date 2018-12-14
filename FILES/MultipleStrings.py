# IN THIS CASE THE USE WE SPECIFY A PARTICULAR CHARACTER WHEN HE DONE TYPING IT CAN BE A FULL STOP(.) OR ANYTHING


file = open("MULTIPLE STRINGS.txt", "x")
print("Enter the text (Type . when you are done) ")

char = ''
while char != '.':
    char = input()
    file.write(char+'\n')




file.close()
