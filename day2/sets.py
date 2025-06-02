#Sets are type of collections
#The main difference between sets and other collections is that sets is 
#UNORDERED -> sets do not recored element position 
#Sets have UNIQUE elements
#To define a sets we use curly brakets{}

sets = {"anuj", 1, True, "yoo ", "yoo "}
print(sets, type(sets))
sets.add("anuj")
print(sets)

#we can convert list to sets using typecasting
lists = ['anuj', 'anuj', 2, True, True]
newSet = set(lists)
print(newSet)

#Set operations
newSet.add("Rajasthan")
newSet.remove(True)

print("Rajasthan" in newSet)  #To check if element is present in set or not     
#Intersection and Union
set1 = sets&newSet
set2 = sets|newSet  #can also be done by set2 = sets.union(newSet)

print(set1, set2)

#To check if a set is a subset of another set
print(set1.issubset(newSet))
