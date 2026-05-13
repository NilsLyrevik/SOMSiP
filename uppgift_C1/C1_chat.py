import nidaqmx
import numpy as np
import time

# ============================================
# Staircase waveform generator for NI DAQ card
# ============================================

# Create staircase values:
# -10 -> +10 -> -10
up = np.arange(-10, 11, 2)      # Rising staircase
down = np.arange(8, -11, -2)    # Falling staircase

waveform = np.concatenate((up, down))

# Time between steps (seconds)
dt = 0.01

# Create DAQ task
task = nidaqmx.Task()

# Analog output channel
task.ao_channels.add_ao_voltage_chan("Dev1/ao0",min_val=-10.0, max_val=10.0)

try:
    while True:
        for value in waveform:
            task.write(value)
            print(f"Output voltage: {value} V")
            time.sleep(dt)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    # Set output to 0 V before closing
    task.write(0.0)
    task.close()