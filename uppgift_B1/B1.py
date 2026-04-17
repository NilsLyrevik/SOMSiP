import pyvisa as pv
import time
rm = pv.ResourceManager()
print(rm.list_resources())


sladd = rm.open_resource('GPIB0::10::INSTR')
#print (sladd.query("*IDN?"))

#print(sladd.query("DISPlay?"))
sladd.write('DISPlay:TEXT "NILS LYREVIK"')

time.sleep(10)
# efter att programmet körts så exitar pyvisa automatiskt 