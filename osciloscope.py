import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Osciloscope")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        controls = ttk.LabelFrame(self, text="Signal Controls")
        controls.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Waveform selector
        ttk.Label(controls, text="Waveform:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.waveform = tk.StringVar(value="Sine")
        waveform_menu = ttk.Combobox(controls, textvariable=self.waveform, values=["Sine", "Square", "Triangle", "Sawtooth"], state="readonly", width=10)
        waveform_menu.grid(row=0, column=1, padx=5, pady=5)

        # Frequency
        ttk.Label(controls, text="Frequency (Hz):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.frequency_entry = ttk.Entry(controls)
        self.frequency_entry.insert(0, "1000")
        self.frequency_entry.grid(row=0, column=3, padx=5, pady=5)

        # Pulse Width
        ttk.Label(controls, text="Pulse Width (s):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.pulse_width_entry = ttk.Entry(controls)
        self.pulse_width_entry.insert(0, "0.5")
        self.pulse_width_entry.grid(row=1, column=1, padx=5, pady=5)

        # Amplitude
        ttk.Label(controls, text="Amplitude:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.amplitude_entry = ttk.Entry(controls)
        self.amplitude_entry.insert(0, "1.0")
        self.amplitude_entry.grid(row=1, column=3, padx=5, pady=5)

        # Duty Cycle
        ttk.Label(controls, text="Duty Cycle (%):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.duty_cycle_entry = ttk.Entry(controls)
        self.duty_cycle_entry.insert(0, "50")
        self.duty_cycle_entry.grid(row=2, column=1, padx=5, pady=5)

        submit_button = ttk.Button(controls, text="Plot Waveform", command=self.plot_waveform)
        submit_button.grid(row=2, column=3, padx=5, pady=5)

        self.fig = plt.Figure(figsize=(5, 4), dpi=120)
        self.plot = self.fig.add_subplot(1, 1, 1)
        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def plot_waveform(self):
        try:
            frequency = float(self.frequency_entry.get())
            amplitude = float(self.amplitude_entry.get())
            duty_cycle = float(self.duty_cycle_entry.get())
            pulse_width = float(self.pulse_width_entry.get())
            waveform = self.waveform.get()
            time_values = np.linspace(0, 1, 1000)
            if waveform == "Sine":
                y_values = amplitude * np.sin(2 * np.pi * frequency * time_values)
            elif waveform == "Square":
                y_values = amplitude * np.where((time_values % (1/frequency)) < (duty_cycle/100)*(1/frequency), 1, -1)
            elif waveform == "Triangle":
                y_values = amplitude * (2 * np.abs(2 * ((time_values * frequency) % 1) - 1) - 1)
            elif waveform == "Sawtooth":
                y_values = amplitude * (2 * ((time_values * frequency) % 1) - 1)
            else:
                y_values = np.zeros_like(time_values)
            self.plot.clear()
            self.plot.plot(time_values, y_values, color='blue', label=f'{waveform} Wave')
            self.plot.set_xlabel('Time (s)')
            self.plot.set_ylabel('Amplitude')
            self.plot.set_title(f'{waveform} Waveform')
            self.plot.legend()
            self.fig.canvas.draw()
        except ValueError:
            print("Invalid input. Please enter numeric values for all fields.")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
