import math

a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
c = int(input("Enter number c:"))


discriminant = (b**2)-(4*a*c)


if discriminant < 0:
    print("Quadratic function has imaginary roots")
else:
    print("The first root is:" + str(-b+(math.sqrt(discriminant))))
    print("The second root is:" + str(-b-(math.sqrt(discriminant))))