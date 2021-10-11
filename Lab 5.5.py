# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

def get_bonus(sa, so):
    if(so>1000):
        bonus=sa*0.2
    elif(so>501 and so<1000):
        bonus=sa*0.1
    return bonus

def nett_salary(sa, bo):
    nett = sa+bo
    return nett

def display(i, sa, so, bo, n):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("            SALARY SLIP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID               :  {}".format(i))
    print("Staff Salary           :  RM {:.2f}".format(sa))
    print("Staff Sold             :  {}".format(so))
    print("Bonus                  :  RM {:.2f}".format(bo))
    print("Nett Salary            :  RM {:.2f}".format(n))

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("            DATA ENTRY")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    s_id     = input("Enter staff id          : ")
    salary = float(input("Enter staff salary      : RM "))
    sold  = int(input("Enter total units sold  : "))
    bonus = get_bonus(salary, sold)
    nett  = nett_salary(salary, bonus)
    display(s_id, salary, sold, bonus, nett)

main()