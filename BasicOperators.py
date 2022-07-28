#Arigmetic Operations
#Basic operations
from re import S


number = 1 + 2 * 3 / 4.0 - 5
print (number)

#the module % returns the remainder of a division
remainder = 11 % 3
print(remainder)

#Using two multiplication symbols makes a power relationship
squared =   7**2
cube = 2**3
print(squared)
print(cube)

#Operators with strings
helloWorld = "Hola" + " " + "mundo!"
print(helloWorld)

#You can also multiply strings
lotsHellos = "Hello" * 10
print(lotsHellos)

#Operators with lists
evenNumbers = [2, 4, 6, 8]
oddNumbers = [1, 3, 5, 7, 9]
allNumbers = evenNumbers + oddNumbers
print(allNumbers)

#You can also multiply lists
print([1, 2, 3] * 3)

#Exercise
# The target of this exercise is to create two lists called x_list and y_list, 
# which contain 10 instances of the variables x and y, respectively. 
# You are also required to create a list called big_list, which contains the 
# variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")