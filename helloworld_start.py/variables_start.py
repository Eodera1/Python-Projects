# Basic data types in Python: Numbers, Strings, Lists, Tuples, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one": 1, "b": 2, "c": 3}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# # re-declaring a variable works
# myint = "abc"
# print(myint)

# dictionaries are accessed via keys
# print(mydict["one"])

# ERROR: variables of different types cannot be combined
print("string type " + str(123))

# Global vs. local variables in functions
def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)


