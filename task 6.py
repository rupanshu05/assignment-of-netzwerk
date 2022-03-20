##task 6
##add and remove elements from a tuple.
##tuple are immutable
##so convert the tuple into list,do the required operations
##and then change the list int tuple

cars =("a","b","c")
a = list(cars)
print(a)

var = ["a","b","c"]
var.append("d")
print(var)

var = ["a","b","c"]
del var[0]
print(var)

cars =["a","b","c"]
a = tuple(cars)
print("list to tuple", a)
