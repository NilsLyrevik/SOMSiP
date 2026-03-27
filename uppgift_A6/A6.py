import math as mt
import matplotlib.pyplot as plt

def f(I_S, U_T, U_D): 
    I_D = I_S*(mt.exp(U_D/U_T)-1)
    return I_D

if __name__ == "__main__":
    # 1 x 10^-8
    input_I_S = 1e-8
    # 25 mV
    input_U_T = 25e-3
    # from 0 to 0.75 volt (20 values)
    x_values = []
    y_values = []
    for i in range(0,20):
        input_U_D = (i*0.75)/19
        x_values.append(input_U_D)
        y_values.append(f(input_I_S, input_U_T, input_U_D))

    # plot the graph
    plt.plot(x_values, y_values)
    plt.xlabel("U_D (V)")
    plt.ylabel("I_D (A)")
    plt.title("I_D as a function of U_D")
    # Kommentera reden uner för att inte visa grafen!
    plt.show()
