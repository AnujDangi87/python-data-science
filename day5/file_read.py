#different modes - r, w, a
file = open("./readme.txt", "r")

print(file.read(3)) #to read five characters
print(file.name)
print(file.mode)

print(file.close())

#if we use open() to open a file we always have to close the file
#insted we can use with open() which automatically closes the file

with open("./readme.txt", "r") as file:
    text = file.readline()
    print(file.readline())
    print(text)

with open("./readme.txt", "r") as file:
    for line in file:
        print(line)

print(file.closed)
print(text) #the variable initialized inside with operator can be used outside

#Looping through lines: Typically, you use a loop to read lines until no more lines are left. t's like reading the entire book, line by line.

while True:
    line = file.readline()
    if not line:
        break  # Stop when there are no more lines to read
    print(line)