#% Operator we can use it with %s or %d
name = "John"
print("Helo %s!" % name)

#To specify two or more arguments we use a tuple ( )
name = "John"
age  = 25
print("He is %s and he is %d years old" % (name, age))

myList = [1, 2, 3]
print("A list: %s" % myList)

#Basic argument
#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#%x/%X - Integers in hex representation (lowercase/uppercase)

#Exercise
#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%f"
formatString = ("Hello")

print(formatString + " %s %s. Your current balance is $%f" % (data))
print(format_string % (data))