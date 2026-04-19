#IMPORTS
import pyvisa as pv
import time
import matplotlib.pyplot as plt
import numpy as np

# -------- HELPERS ---------

def p(T_b,T_ä,index) -> float:
    k = 0.001 # TESTA DIG FRAM
    e = T_b - T_ä
    reglerspänning = e * k
    print(reglerspänning+ " at index: " + str(index))
    return reglerspänning

def logicLoop():
    Tbör = 25 #celcius men vad ska värdet vara fråga på labb
    Tär  = sladd34.query("något commando som fungerar för att mäta temp")
    spänning = 10 #STARTSPÄNNING
    while True:
        spänning = p(Tbör,Tär,index)
        sladdE3.write("något commando som fungerar för att sätta spänning " + str(spänning))
        time.sleep(0.5)

# -------- END HELPERS ---------

rm = pv.ResourceManager()
print(rm.list_resources())

sladdE3 = rm.open_resource('GPIB0::10::INSTR') # DENNA KANSKE INTE STÄMMER KOLLA MED PRINT på Line 5
print(sladdE3.query("*IDN?"))
sladd34 = rm.open_resource('GPIB0::11::INSTR') # DENNA KANSKE INTE STÄMMER KOLLA MED PRINT på Line 5
print(sladd34.query("*IDN?"))
time.sleep(10)

#logik

logicLoop()

sladdE3.close()
sladd34.close()
rm.close()

