def f():
    x = int(input("input a integer:"))

    remainder = x % 2

    if remainder:
        print("The integer is odd.")
    else:
        print("The integer is even.")

if __name__ == "__main__": # gör så att filen kan köras med >python A1.py
    f()
