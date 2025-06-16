file = open("./write.txt", "w")

file.write("This is line 1\n")
file.write("This is line 2")

file.close()

# appending
with open("./write.txt", "a") as file:
    lines = ["this is line 1a\n", "this is line 2a"]

    for line in lines:
        file.write(line)

#copy content from one file to another
with open("./readme.txt", "r") as readFile:
    with open("./write.txt", "w") as writeFile:
        for line in readFile:
            writeFile.write(line)



