# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

hourly_rate = 6.50

hour=int(input("Enter how many hours you work for this week: "))

if(hour < 1):
    print("Invalid input")
else:
    if(hour < 40):
        salary = (hourly_rate*hour)
    if(hour > 40):
        salary = (hourly_rate*40) + ((hour-40)*10.50)
    if(hour > 60):
        salary = (hourly_rate*40) + (20*10.50)
        print("Maximum work time per week is 60 hours.")
        print("So only additional 20 hours is calculated for overtime pay.")
    print("Your salary is RM {:.2f}".format(salary))