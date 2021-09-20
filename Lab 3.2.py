# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

cur_balance = 30.12

print("Please withdraw money")
money = float(input("\nEnter amount of money to withdraw: "))
total = cur_balance-money
if total < 10:
    print("There is no sufficient fund")
    print("Your current balance is RM {:.2f}.".format(cur_balance))
else:
    print("Current balance is sufficient")
    print("Your current balance is RM {:.2f}.".format(total))