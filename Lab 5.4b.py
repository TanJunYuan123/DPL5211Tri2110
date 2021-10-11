# student ID: 1201200431 #
# student Name: Tan Jun Yuan #

def rectangle(w, l):
    rectangle = w*l
    return rectangle

def triangle(w, l):
    triangle = (w*l)/2
    return triangle

def main():
    i=0
    while i<2:
        width =float(input("Enter width   : "))
        length=float(input("Enter length  : "))
        r=rectangle(width, length)
        t=triangle(width, length)

        print("\nRectangle area : {:.2f}".format(r))
        print("Triangle area  : {:.2f}\n\n\n".format(t))
        i+=1

main()