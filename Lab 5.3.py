# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("\nEnter centimeter : "))
    m = cm_to_meter(cm)
    print("\n{:.2f} centimeters equals to {:.2f} meters ".format(cm, m))

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

def get_meter():
    m = float(input("\nEnter meter : "))
    cm = meter_to_cm(m)
    print("\n{:.2f} meters equals to {:.2f} centimeters ".format(m, cm))

def main():
    print("======================================")
    print("                MENU")
    print("======================================")
    print("  1.    Convert centimeter to meter")
    print("  2.    Convert meter to centimeter")
    print("======================================")
    choice=input("Enter your choice : ")
    if(choice=='1'):
        get_cm()
    elif(choice=='2'):
        get_meter()
    else:
        print("Invalid choice")

main()
