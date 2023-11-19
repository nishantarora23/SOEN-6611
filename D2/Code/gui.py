import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askinteger
import matplotlib.pyplot as plt
from MetricsticsMain import *
from tkinter import filedialog
import random


class MetricsApp:
    def __init__(self, master):
        self.master = master
        master.title("METRICSTICS")

        # GUI setup
        style = ttk.Style()
        style.configure('TButton', borderwidth=2,
                        relief="groove", foreground="black")

        options_frame = tk.Frame(master)
        options_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        options_label = ttk.Label(options_frame, text="Options:")
        options_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        options = ["Minimum", "Maximum", "Mode", "Median", "Mean",
                   "Mean Absolute Deviation", "Standard Deviation"]
        self.option_var = tk.StringVar(value=options[0])
        option_menu = ttk.Combobox(
            options_frame, textvariable=self.option_var, values=options, state="readonly", width=25)
        option_menu.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")

        random_data_button = ttk.Button(options_frame, text="Generate Random Data", command=self.generate_random_data,
                                        width=25)
        random_data_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        upload_button = ttk.Button(
            options_frame, text="Upload File", command=self.upload_file, width=25)
        upload_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        right_frame = tk.Frame(master)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

        visualize_button = ttk.Button(
            options_frame, text="Visualize Data", command=self.visualize_data, width=25)
        visualize_button.grid(row=4, column=0, padx=5, pady=5)

        self.export_button = ttk.Button(
            options_frame, text="Export Data", command=self.export_data_to_csv, width=25)
        self.export_button.grid(
            row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        label_data = ttk.Label(
            right_frame, text="Enter data (comma-separated):")
        label_data.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_data = tk.Text(right_frame, height=5, width=50)
        self.entry_data.grid(row=1, column=0, padx=5, pady=5)

        bottom_frame = tk.Frame(master)
        bottom_frame.grid(row=1, column=0, columnspan=2,
                          padx=10, pady=10, sticky="s")

        calculate_button = ttk.Button(
            bottom_frame, text="Calculate Statistics", command=self.calculate_statistics)
        calculate_button.grid(row=0, column=0, padx=5, pady=5)

        clear_button = ttk.Button(
            bottom_frame, text="Clear Data", command=self.clear_data)
        clear_button.grid(row=0, column=1, padx=5, pady=5)

        self.result_text = tk.StringVar()
        result_label = ttk.Label(bottom_frame, textvariable=self.result_text)
        result_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        help_button = ttk.Button(master, text="Help", command=self.show_help)
        help_button.grid(row=0, column=1, padx=5, pady=5, sticky="ne")

        self.export_button = ttk.Button(bottom_frame, text="Export to CSV")
        self.export_button.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.export_button.grid_remove()

    def generate_random_data(self):
        # Prompt the user for the number of data points
        num_data_points = askinteger(
            "Generate Random Data", "Enter the number of data points (1-1000):", minvalue=1, maxvalue=2500)
        if num_data_points is None:
            # User clicked cancel
            return

        random_data = [round(random.uniform(0, 100), 2)
                       for _ in range(num_data_points)]
        self.entry_data.delete("1.0", tk.END)
        self.entry_data.insert(tk.END, ', '.join(map(str, random_data)))

    def calculate_statistics(self):
        selected_option = self.option_var.get()
        data = self.entry_data.get("1.0", tk.END)
        data = data.split(',')
        data = [float(x.strip()) for x in data if x.strip()]
        result = MetricsticsMain.calculate_metricstics(data, selected_option)
        if selected_option.strip() == 'Mode':
            self.result_text.set(result)
        else:
            label, numeric_value = result.split(':')
            numeric_value = numeric_value.strip()
            if '.' in numeric_value and len(numeric_value.split('.')[1]) > 2:
                rounded_numeric_value = round(float(numeric_value), 3)
                rounded_result = f"{label.strip()}: {rounded_numeric_value}"
            else:
                rounded_result = f"{label.strip()}: {numeric_value}"
            self.result_text.set(rounded_result)
        self.export_button.grid(
            row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        export_data = {"Data": data, "Statistic": selected_option}
        self.export_button.config(
            command=lambda: self.export_to_csv(export_data))

    def export_to_csv(self, data_dict):
        self.result_text.set(MetricsticsMain.export_to_csv(data_dict))

    def clear_data(self):
        self.entry_data.delete("1.0", tk.END)

    def show_help(self):
        help_window = tk.Toplevel(self.master)
        help_window.title("Help")

        help_text = """Welcome to METRICSTICS!

    1. Options: 
        Choose a statistical measure from the drop-down menu.
    2. Generate Random Data: 
        Click to fill the data field with random numbers.
    3. Enter Data: 
        Manually enter numbers, separated by commas.
    4. Calculate: 
        Click to see the result based on your chosen measure.
    5. Clear Data: 
        Reset the data entry field.
    6. Export to CSV: 
        Save data and result to CSV.

    Thank you for using METRICSTICS!"""

        help_label = ttk.Label(help_window, text=help_text,
                               wraplength=400, justify='left')
        help_label.pack(padx=20, pady=20)

        close_button = ttk.Button(
            help_window, text="Close", command=help_window.destroy)
        close_button.pack(pady=10)

    def upload_file(self):
        # Open a file dialog to choose a file
        file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=[("Text files", "*.txt")])

        # Read the content of the selected file and insert it into the entry_data Text widget
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.entry_data.delete("1.0", tk.END)
                self.entry_data.insert(tk.END, file_content)

    # Store the entered data

    # Modify the export_to_csv method
    def export_data_to_csv(self):
        data = self.entry_data.get("1.0", tk.END).strip()
        if data:
            data_list = [float(x.strip())
                         for x in data.split(',') if x.strip()]

            # Create a CSV file with data
            filename = "exported_data.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # writer.writerow(["Exported Data"])
                writer.writerow(data_list)

            self.result_text.set(f"Data exported to {filename}")
        else:
            self.result_text.set("No data to export.")

    # Visualise Data

    def visualize_data(self):
        data = self.entry_data.get("1.0", tk.END)
        data = data.split(',')
        data = [float(x.strip()) for x in data if x.strip()]

        self.plot_histogram(data)
        self.plot_box_plot(data)
        self.plot_line_chart(data)
        self.plot_scatter_plot(data)

    def plot_histogram(self, data):
        plt.hist(data, bins=10, edgecolor='black')
        plt.title('Histogram')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

    def plot_box_plot(self, data):
        plt.boxplot(data)
        plt.title('Box Plot')
        plt.xlabel('Data')
        plt.ylabel('Values')
        plt.show()

    def plot_line_chart(self, data):
        x_values = list(range(1, len(data) + 1))
        plt.plot(x_values, data, marker='o')
        plt.title('Line Chart')
        plt.xlabel('Data Point')
        plt.ylabel('Value')
        plt.show()

    def plot_scatter_plot(self, data):
        x_values = list(range(1, len(data) + 1))
        plt.scatter(x_values, data)
        plt.title('Scatter Plot')
        plt.xlabel('Data Point')
        plt.ylabel('Value')
        plt.show()
