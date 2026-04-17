import pyvisa as pv
import time

rm = pv.ResourceManager()
print(rm.list_resources())

sladd = rm.open_resource('GPIB0::10::INSTR')
sladdusb = rm.open_resource('USB0::0x0957::0x0407::MY44013136::INSTR')

print("GPIB QUERY ÄR " ,sladdusb.query("*IDN?"))
print("USB QUERY ÄR " ,sladdusb.query("*IDN?"))