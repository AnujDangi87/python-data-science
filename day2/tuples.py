#Tuples are an ordered sequence but are immutable
#Tuples are represented with parenthesis
#Tuples are referenced objects(Aliasing)

tuple1 = ("disco", 3, 'a')

print(tuple1)
print(type(tuple1))
print(tuple1[1])

#two tuples can be added using +

tuple2 = ("hello", 123) + tuple1
print(tuple2)

#We can perform operations like slicing, length on tuple
print(tuple2[0:3])
print(len(tuple2))

#tuples are unmutabble
#Tuples can be nested
tuple3 = (tuple1, tuple2)

print(tuple3[0][0])

