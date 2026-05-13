import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
from nidaqmx.constants import Edge
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Inställningar
# ============================================================
SAMP_RATE    = 5000   # Hz  (≫ 2 × 130 Hz → ingen vikning)
NUMB_OF_SAMP = 500    # 500 / 5000 = 0.1 s ≈ 13 perioder av 130 Hz

# ============================================================
# Hårdvarukoppling
#   FG utgång  →  DAQ ai0  (RSE, jordreferens)
#   FG Sync    →  DAQ PFI0 (TTL-puls, en puls per period)
#
# Sync-pulsen startar varje datainsamling vid exakt samma
# fasvinkel (0°) → signalen "fryser" i plottfönstret.
# ============================================================

def del_b_triggad():
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 4))
    t = np.linspace(0, NUMB_OF_SAMP / SAMP_RATE * 1000, NUMB_OF_SAMP)  # ms
    line, = ax.plot(t, np.zeros(NUMB_OF_SAMP), linewidth=1.5)
    ax.set_title(
        "C4b – Triggad live-mätning  (130 Hz sinus, 2 Vpp) | Ctrl+C för att avsluta\n"
        "Sync → PFI0  |  Datainsamling startar vid stigande flank → fas låst vid 0°"
    )
    ax.set_xlabel("Tid [ms]")
    ax.set_ylabel("Spänning [V]")
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True)
    plt.tight_layout()

    try:
        while True:
            # Ett nytt Task per varv säkerställer att triggern
            # återställs och väntar på nästa Sync-puls.
            with nidaqmx.Task() as task:

                # --- Kanal ---
                task.ai_channels.add_ai_voltage_chan(
                    "Dev1/ai0",
                    min_val=-10.0,
                    max_val=10.0,
                    terminal_config=TerminalConfiguration.RSE
                )

                # --- Timing: ändligt antal sampel med hårdvaruklocka ---
                task.timing.cfg_samp_clk_timing(
                    SAMP_RATE,
                    sample_mode=AcquisitionType.FINITE,
                    samps_per_chan=NUMB_OF_SAMP
                )

                # --- Digital starttrigger på PFI0, stigande flank ---
                # FG:ns Sync-utgång ger en TTL-puls i fas med sinusen (0°).
                # Insamlingen startar exakt vid denna puls → konstant fasläge.
                task.triggers.start_trigger.cfg_dig_edge_start_trig(
                    "/Dev1/PFI0",
                    Edge.RISING
                )

                task.start()
                data = task.read(READ_ALL_AVAILABLE)
                task.stop()

            # --- Uppdatera plot ---
            line.set_ydata(data)
            fig.canvas.draw()
            fig.canvas.flush_events()

    except KeyboardInterrupt:
        pass

    print("Mätningen avslutad")
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    del_b_triggad()