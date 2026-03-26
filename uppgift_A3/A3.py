def f():
    # Prompt the user to enter two comma-separated resistor values
    prompt = "Enter two comma-separated resistor values (ohm): "
    # Split the input into two parts and convert them to floats
    r1_s, r2_s = input(prompt).split(",")
    # Convert the string inputs to floats
    r1 = float(r1_s)
    r2 = float(r2_s)

    # formula = 1/R = 1/r1 + 1/r2
    # Calculate the equivalent resistance using the formula for parallel resistors
    r = 1 / (1/r1 + 1/r2)
    # Convert the equivalent resistance to an integer
    r_i = int(r)

    # Print the equivalent resistance in ohms
    print("The equivalent resistance is (ohm): ", r_i)

# This allows the file to be run as a script >python3 A2.py
if __name__ == "__main__":
    # this calls the function f() when the script is executed
    f()