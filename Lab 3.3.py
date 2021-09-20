# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

mark = int(input("Enter your mark: "))
if (mark > 80 and mark <= 100):
    grade='A'
    print("Your grade is {}".format(grade))
elif(mark > 70 and mark <= 100):
    grade='B'
    print("Your grade is {}".format(grade))
elif(mark < 50 and mark >= 0):
    grade='fail'
    print("Your grade is {}".format(grade))
else:
    print("Invalid mark given")