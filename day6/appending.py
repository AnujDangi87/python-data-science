# tell() returns the current position in bytes
# seek(offset, from) - changes the position by "offset" bytes with respect to 'from'
with open("./file.txt", "a+") as f:
    print("Initial location : {}".format(f.tell()))

    data = f.read()
    if(not data):   #empty string return false in python
        print('Read nothing')
    else:
        print(f.read())

    f.seek(0, 0) #move 0 byte from beginning.

    print("\nNew location : {}".format(f.tell()))
    data = f.read()

    if(not data):
        print("Read nothing")
    else:
        print(data)

    print("Location after read : {}".format(f.tell()))