import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import time

# Skapa task
# Skapa task
task = nidaqmx.Task()

# Lägg till analog ingång i RSE-mode
task.ai_channels.add_ai_voltage_chan(
    "Dev1/ai0",
    min_val=0.0,
    max_val=5.0,
    terminal_config=TerminalConfiguration.RSE
)

print("Mäter spänning... Tryck Ctrl+C för att stoppa.")

try:
    while True:
        voltage = task.read()
        print(f"Spänning: {voltage:.3f} V")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Avslutar mätning.")

finally:
    task.close()