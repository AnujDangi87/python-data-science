#Python is a interpreted language(it executes line by line)

print("hello, world")   #print statment
#Comments

z = 2 + 15  #sumation
print(z)

#Python is an weakly typed language -> we don't have to tell python what datatype we are using 
# dataTypes in python -> int, float, bool other classes -> str
a = 5.9
print(type(a))

#TypeCasting
b = int(a)
print(type(b))
print(b)
print(type("Hello"))

#For concatenation in python use ,
print(1, "hello")

#Python is an object oriented language

#type(6/2) -> float 
#// -> integer division(floor division)

variable = 4.55

#Python executes airthmetic operations on basis of div, mul, sub ,add

#Sting in Python
name = "Anuj Dangi"
print(name[0], name[-1])    #-index prints values start form end
print(name[0:4], name[::2])
print(name[0:2:4])
print("Length of the String :",len("Anuj") )

#replicating strings
string = "abcd"
newStr = 3*string
print(newStr)
#Stirngs are immutable in nature in python
#Strings methods 
newStr.upper()
print(newStr.find("A"))