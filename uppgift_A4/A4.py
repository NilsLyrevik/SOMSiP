import math as mt

def f():
    # input statement
    r = float(input("input radius > "))

    # calculate the area of a circle
    area = mt.pi * r**2
    print("area of a circle with radius", r, "is", area)

if __name__ == "__main__":
    f()
