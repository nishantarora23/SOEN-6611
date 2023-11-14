import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from statistics import calculate_statistics, export_to_csv
import random

class MetricsApp:
    def __init__(self, master):
        self.master = master
        master.title("METRICSTICS")

        # GUI setup
        style = ttk.Style()
        style.configure('TButton', borderwidth=2, relief="groove", foreground="black")

        options_frame = tk.Frame(master)
        options_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        options_label = ttk.Label(options_frame, text="Options:")
        options_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        options = ["Minimum", "Maximum", "Mode", "Median", "Mean", "Mean Absolute Deviation", "Standard Deviation"]
        self.option_var = tk.StringVar(value=options[0])
        option_menu = ttk.OptionMenu(options_frame, self.option_var, *options)
        option_menu.config(width=25)  
        option_menu.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")

        random_data_button = ttk.Button(options_frame, text="Generate Random Data", command=self.generate_random_data, width=25)
        random_data_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        right_frame = tk.Frame(master)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

        label_data = ttk.Label(right_frame, text="Enter data (comma-separated):")
        label_data.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_data = tk.Text(right_frame, height=5, width=50)
        self.entry_data.grid(row=1, column=0, padx=5, pady=5)

        bottom_frame = tk.Frame(master)
        bottom_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="s")

        calculate_button = ttk.Button(bottom_frame, text="Calculate Statistics", command=self.calculate_statistics)
        calculate_button.grid(row=0, column=0, padx=5, pady=5)

        clear_button = ttk.Button(bottom_frame, text="Clear Data", command=self.clear_data)
        clear_button.grid(row=0, column=1, padx=5, pady=5)

        self.result_text = tk.StringVar()
        result_label = ttk.Label(bottom_frame, textvariable=self.result_text)
        result_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        help_icon = tk.PhotoImage(file="help.png")
        help_button = ttk.Button(master, image=help_icon, style='IconButton.TButton')
        help_button.grid(row=0, column=1, sticky="ne")

        style.configure('IconButton.TButton', borderwidth=0)
        help_button.bind("<Button-1>", lambda e: self.show_help())

        self.export_button = ttk.Button(bottom_frame, text="Export to CSV")
        self.export_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.export_button.grid_remove()

    def generate_random_data(self):
        num_data_points = random.randint(5, 20)
        random_data = [round(random.uniform(0, 100), 2) for _ in range(num_data_points)]
        self.entry_data.delete("1.0", tk.END)  
        self.entry_data.insert(tk.END, ', '.join(map(str, random_data)))

    def calculate_statistics(self):
        selected_option = self.option_var.get()
        data = self.entry_data.get("1.0", tk.END)
        data = data.split(',')
        data = [float(x.strip()) for x in data if x.strip()]
        
        self.result_text.set(calculate_statistics(data, selected_option))

        self.export_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        export_data = {"Data": data, "Statistic": selected_option}
        self.export_button.config(command=lambda: self.export_to_csv(export_data))

    def export_to_csv(self, data_dict):
        self.result_text.set(export_to_csv(data_dict))

    def clear_data(self):
        self.entry_data.delete("1.0", tk.END)

    def show_help(self):
        help_window = tk.Toplevel(self.master)
        help_window.title("Help")
        
        help_text = """
        This section needs to be updated after discussion
        """
        
        help_label = ttk.Label(help_window, text=help_text, wraplength=400, justify='left')
        help_label.pack(padx=20, pady=20)
        
        close_button = ttk.Button(help_window, text="Close", command=help_window.destroy)
        close_button.pack(pady=10)