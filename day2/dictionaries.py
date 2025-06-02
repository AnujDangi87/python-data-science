#Data is stored as key:value pair in dictionaries
#dictionaries is denoted with curly brackets {}
#The keys in dictionaries have to unique and immutable
#The value can be immutable, mutable, duplicates
#The pair of key:value is separated by comma

dictionary = {"name":"anuj","age":22}
print(dictionary, dictionary["age"])

#To add
dictionary["gender"] = "male"
print(dictionary)
#To delete
del(dictionary["gender"])
print(dictionary)

#TO check if a key is present or not
print("name" in dictionary)

#To print all the keys
print(dictionary.keys())        #The output will be list like object

#To print all the values
print(dictionary.values())  #list like object

list(dictionary.keys())     #Returns a list object of keys