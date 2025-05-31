name = "anuj"
age = 21
#Known as string interpolation or fString #also we can do airthmetic operation inside {}
print(f"my name is {name} and age is {age}")

#Oldest way same as in c language
print("my name is %s and age is %d"%(name, age))

#str.format
print("my name is {} and age is {}".format(name, age))

#raw String r'' ->will evaluate \ as a char not as sequence char
string = "C:\new_folder\file.txt"
print(string)

raw_string = r"C:\new_folder\file.txt"
print(raw_string)