import pyvisa as pv
import time
rm = pv.ResourceManager()
print(rm.list_resources())
sladd = rm.open_resource('GPIB0::10::INSTR')

sladd.write("OUTPUT ON")

for i in range(5,15):
     curr_freq = "FREQ " + str(i*100)
     print(curr_freq)
     sladd.write(curr_freq)
     time.sleep(0.5)
print("Done")

sladd.write("OUTPUT OFF")