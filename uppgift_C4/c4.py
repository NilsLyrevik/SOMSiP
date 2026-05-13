import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Inställningar
# ============================================================
SAMP_RATE    = 5000   # Hz  – Nyquist: minst 2 × 130 Hz = 260 Hz, vi tar god marginal
NUMB_OF_SAMP = 500    # Antal punkter per insamling (~100 ms fönster vid 5000 Hz)
# Med 5000 Hz och 500 punkter fångar vi 500/5000 = 0.1 s  ≈ 13 perioder av 130 Hz-signalen

# ============================================================
# Del a – Engångsinsamling + plot
# ============================================================
def del_a():
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(
            "Dev1/ai0",
            min_val=-10.0,
            max_val=10.0,
            terminal_config=TerminalConfiguration.RSE   # Jordrelaterat (RSE)
        )
        task.timing.cfg_samp_clk_timing(
            SAMP_RATE,
            sample_mode=AcquisitionType.FINITE,
            samps_per_chan=NUMB_OF_SAMP
        )
        data = task.read(READ_ALL_AVAILABLE)

    # Skapa tidsaxel
    t = np.linspace(0, NUMB_OF_SAMP / SAMP_RATE, NUMB_OF_SAMP)

    plt.figure(figsize=(10, 4))
    plt.plot(t * 1000, data, marker='o', markersize=2, linewidth=1)
    plt.title("Del a – Engångsinsamling  (130 Hz sinus, 2 Vpp, RSE)")
    plt.xlabel("Tid [ms]")
    plt.ylabel("Spänning [V]")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ============================================================
# Del b – Kontinuerlig insamling i while-loop med live-plot
#          Avsluta med Ctrl+C  →  "Mätningen avslutad" printas
# ============================================================
def del_b():
    plt.ion()                          # Interaktivt läge – möjliggör live-uppdatering
    fig, ax = plt.subplots(figsize=(10, 4))
    t = np.linspace(0, NUMB_OF_SAMP / SAMP_RATE, NUMB_OF_SAMP)
    line, = ax.plot(t * 1000, np.zeros(NUMB_OF_SAMP), linewidth=1)
    ax.set_title("Del b – Live-mätning  (130 Hz sinus, 2 Vpp, RSE) | Ctrl+C för att avsluta")
    ax.set_xlabel("Tid [ms]")
    ax.set_ylabel("Spänning [V]")
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True)
    plt.tight_layout()

    try:
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(
                "Dev1/ai0",
                min_val=-10.0,
                max_val=10.0,
                terminal_config=TerminalConfiguration.RSE
            )
            task.timing.cfg_samp_clk_timing(
                SAMP_RATE,
                sample_mode=AcquisitionType.CONTINUOUS   # Kontinuerlig insamling
            )
            task.start()

            while True:
                # Läs NUMB_OF_SAMP nya mätvärden per varv
                data = task.read(number_of_samples_per_channel=NUMB_OF_SAMP)

                # Uppdatera plotfönstret
                line.set_ydata(data)
                ax.relim()
                ax.autoscale_view(scalex=False)  # Behåll x-axeln fast
                fig.canvas.draw()
                fig.canvas.flush_events()

    except KeyboardInterrupt:
        pass   # Ctrl+C fångad – fortsätt till raden nedan

    print("Mätningen avslutad")
    plt.ioff()
    plt.show()


# ============================================================
# Kör del a eller b genom att kommentera/avkommentera nedan
# ============================================================
if __name__ == "__main__":
    del_a()   # ← Byt till del_b() för del b
    # del_b()