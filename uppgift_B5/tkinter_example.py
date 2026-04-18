import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import pyvisa
import time

def generate_wave():
    try:
        # Get input values
        num_points = int(entry_points.get())
        sampling_freq = float(entry_sampling.get())
        amplitude = float(entry_amplitude.get())
        frequency = float(entry_frequency.get())
        waveform = waveform_var.get()

        

    except ValueError:
        print("Please enter valid numbers.")

# Create window
root = tk.Tk()
root.title("Waveform Generator")

# --- Digitizing Parameters ---
frame_digit = tk.LabelFrame(root, text="Digitizing Parameters")
frame_digit.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_digit, text="Number of Points:").grid(row=0, column=0)
entry_points = tk.Entry(frame_digit)
entry_points.grid(row=0, column=1)

tk.Label(frame_digit, text="Sampling Frequency (Hz):").grid(row=1, column=0)
entry_sampling = tk.Entry(frame_digit)
entry_sampling.grid(row=1, column=1)

# --- Waveform Parameters ---
frame_wave = tk.LabelFrame(root, text="Waveform Parameters")
frame_wave.grid(row=1, column=0, padx=10, pady=10)

tk.Label(frame_wave, text="Amplitude:").grid(row=0, column=0)
entry_amplitude = tk.Entry(frame_wave)
entry_amplitude.grid(row=0, column=1)

tk.Label(frame_wave, text="Frequency (Hz):").grid(row=1, column=0)
entry_frequency = tk.Entry(frame_wave)
entry_frequency.grid(row=1, column=1)

tk.Label(frame_wave, text="Waveform Shape:").grid(row=2, column=0)

waveform_var = tk.StringVar()
waveform_dropdown = ttk.Combobox(
    frame_wave,
    textvariable=waveform_var,
    values=["Sine", "Cosine", "Square", "Triangle","DC-Level","Sawtooth","User Defined"],
    state="readonly"
)
waveform_dropdown.grid(row=2, column=1)
waveform_dropdown.current(0)

# --- Generate Button ---
generate_button = tk.Button(root, text="Submit", command=generate_wave)
generate_button.grid(row=2, column=0, pady=10)

root.mainloop()