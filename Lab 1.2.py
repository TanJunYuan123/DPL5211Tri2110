# Lab 1.2 get input two numbers and display the sum of the two numbers

person = int(input("Please enter a number 1: "))
person2 = int(input("Please enter a number 2: "))

total = person+person2

# print("The total number is ", total)
# The sum of 5 and 6 is 11

print("The sum of",person,"and",person2,"is",total)
print("The sum of {} and {} is {}".format(person,person2,total))