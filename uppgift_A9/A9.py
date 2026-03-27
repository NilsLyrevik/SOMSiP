'''
En snabb kommentar bara!
I uppgiftbeksrivningen står det gör uppgift 8 på sida 15...
för mig ligger uppgiften på sida 13, hoppas att det är korrekt!

Mvh Nils
'''

def f():
    # hämta storhet och enhet
    mag, unit = input("Enter Length in Unit of cm or in (withSpace Separating Magnitude and Unit): ").split(" ")
    # gör om storhet, enhet är redan i strängformat
    mag = float(mag)
    # ifsats logik talar för sig själv!
    if unit == "cm":
        print(f"{mag} cm is {mag/2.54} in")
    elif unit == "in":
        print(f"{mag} in is {mag*2.54} cm")
    else:
        print("Invalid Unit")

if __name__ == "__main__":
    f()
