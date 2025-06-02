#Lists are an ordered sequence
#Lista are represented with square brackets
#List are referenced(Aliasing) objects means if we create a new variable and set it equlas to other list it will point to same list

list1 = [1, 3, "anuj"]

#list can be added using +
#we can also perform operations like slicing, length
#list can also be nested
#The key difference between lists and tuples are that
#List are MUTABLE(just like array)
#we can also access element using negative index also

list1[1] = "konichiwa"
print(list1)

#List can be nested with other list, tuple, int, float, string

#List functions
#extends -> will be taken as multiple list element
list1.extend(["new", "list", 'i see'])
print(list1)

#append -> will be taken as single list element
list1.append(['new', 'append'])
print(list1)

#we can delete elments from list using del 
del(list1[2])
print(list1)

#When performing split operation on string it returns an list
newList = "A,B,C,D".split(",")
print(newList)

#If we want to create a copy of the existing list without making its alias
nAlias = newList[:]

help(nAlias)