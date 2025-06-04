def first_function():
    return "Returned value"

print(first_function())

def add(a):
    return a+10

b = add(5)
print(b)
#Some inbuilt function likes sum(list, tuple, etc)->add all the value of the given collection paramter, len(), sorted(), list.sort()

def add(a, b):
    """
    This is called Documentatin String it tells what the function does
    """
    #you can see documentation string of a function using help(fun)
    help(add)
    return a+b

print(add(1,2))

c = 5#global scoope
#functions have local scope, to make a variable global in function we have to use global

def scope():
    global d
    d= 6
    return

scope()
print(d)
