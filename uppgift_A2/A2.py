def f():
    prompt = "Enter two comma-separated resistor values (ohm): "
    r1_s, r2_s = input(prompt).split(",")
    r1 = float(r1_s)
    r2 = float(r2_s)

    # formula = 1/R = 1/r1 + 1/r2
    r = 1 / (1/r1 + 1/r2)
    r_i = int(r)

    print("The equivalent resistance is (ohm): ", r_i)

if __name__ == "__main__":
    f()