#This is an integer
myInt = 7
print(myInt)

#This is a float
myFloat = 7.0
print('This is float1', myFloat)
myFloat2 = float(7.2)
print('This is float2', myFloat2)

#This is a string
myString = 'First'
print('This is the', myString)
myString2 = "Second"
print('This is the', myString2)

#Doble quotes help us to use apostrophes"
doubleQoutes = "Don't worry about apostrophes"
print(doubleQoutes)


#Simple operations with var and strings
one = 1
two = 2
three = one + two
print(three)

hola = 'hello'
mundo = 'world'
holaMundo = hola + ' ' + mundo
print(holaMundo)

#Multiple assigments in one line
a, b = 3, 4
print(a,b)


#Exercise

# Var definition
myString = "hello"
myFloat = 10.0
myInt = 20

#Code
if myString == 'hello':
    print('My string is %s' % myString)
if isinstance(myFloat, float) and myFloat == 10.0:
    print('My float is %s' % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print('My integer is %s' % myInt)
