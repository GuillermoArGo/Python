#My first List

from re import M


myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[0])
print(myList[1])
print(myList[2])

#Print all the values in list
for x in myList:
    print(x)

#Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica", "Maria"]

#write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

#This code should write out filled arrays and the second name in the list (Eric)
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)