#IMPORTS
import pyvisa as pv
import time
import matplotlib.pyplot as plt
import numpy as np

# -------- HELPERS ---------

def p(T_b,T_ä,index) -> float:
    k = 1.5 # TESTA DIG FRAM
    e = T_b - T_ä
    reglerspänning = e * k
    print(str(reglerspänning)+ " at index: " + str(index))
    return reglerspänning

def logicLoop():
    Tbör = 35 #celcius men vad ska värdet vara fråga på labb
    spänning = 2.0 #STARTSPÄNNING
    index = 0
    while True:
        Tär  = float(sladd34.query('MEAS:TEMP? RTD'))
        print("current temp: " + str(Tär))
        spänning = p(Tbör,Tär,index)
        spänning = min(spänning, 19.9)
        sladdE3.write(f'APPL {spänning:.1f},1.4')
        time.sleep(1.0)
        index += 1

# -------- END HELPERS ---------

rm = pv.ResourceManager()
print(rm.list_resources())

sladd34 = rm.open_resource('USB0::0x2A8D::0x1301::MY53216844::INSTR')
sladdE3 = rm.open_resource('GPIB0::5::INSTR')
print("SladdE3: " ,sladdE3.query("*IDN?"))
print("Sladd34: ", sladd34.query("*IDN?"))
print("sleeping 1 sec")
time.sleep(1)

#logik

logicLoop()

sladdE3.close()
sladd34.close()
rm.close()
