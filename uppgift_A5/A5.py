def f():
    filename = input("input filename > ")
    if filename.endswith(".py"):
        print("filename is a python file")
    else:
        print("filename is not a python file")

if __name__ == "__main__":
    f()