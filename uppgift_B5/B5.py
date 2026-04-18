import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import pyvisa
import time 

def gen():
    try:
        # YÄHNI GÖT NGT
        inst = rm.open_resource(waveform_var.get())
        statement = inst.query(command_entry.get())
        print(statement)
        inst.close()
        # rm.close()
    except ValueError:
        print("Please enter valid numbers.")
# PYVISA LOGIC
rm = pyvisa.ResourceManager()
instrument_list = rm.list_resources() #.tolist()?
if len(instrument_list) == 0:
    print("No instruments found. dummy list created")
    instrument_list = ["ASRL2::INSTR","ASRL3::INSTR"]
print(instrument_list)
## HITTA RÄTT PORT OSV



#TKINTER LOGIC
# Create window
root = tk.Tk()
root.title("Instrument Controller")

# --- instrument finding and stuff ---
frame = tk.LabelFrame(root, text="Label Label Label... ya ge it?")
frame.grid(row=1, column=0, padx=10, pady=10)

tk.Label(frame, text="Command:").grid(row=1, column=0)
command_entry = tk.Entry(frame)
command_entry.grid(row=1, column=1)

tk.Label(frame, text="instruments:").grid(row=2, column=0)

waveform_var = tk.StringVar()
waveform_dropdown = ttk.Combobox(
    frame,
    textvariable=waveform_var,
    values=instrument_list,
    state="readonly"
)
waveform_dropdown.grid(row=2, column=1)
waveform_dropdown.current(0)

# --- Generate Button ---
generate_button = tk.Button(root, text="Submit", command=gen)
generate_button.grid(row=2, column=0, pady=10)

root.mainloop()