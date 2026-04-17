import pyvisa
import time

rm = pyvisa.ResourceManager()
print(rm.list_resources())
## HITTA RÄTT PORT OSV

inst = rm.open_resource('ASRL2::INSTR')
inst.write_termination = '\n'
inst.read_termination = '\n'
inst.baud_rate = 9600
inst.data_bits = 8
inst.parity = 0
inst.flow_control = 0
inst.stop_bits = 20 # 10 = 1 stop bit, 20 = 2 stop bits

for i in range(20):
    inst.write('C')
    time.sleep(0.5) 

inst.close()
rm.close()