import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
import uuid
import matplotlib.pyplot as plt
from MetricsticsMain import *
from tkinter import filedialog
import random
from pathlib import Path


class MetricsApp:
    """Main application class for the METRICSTICS GUI."""

    def __init__(self, master):
        """Initialize the METRICSTICS GUI."""
        self.master = master
        master.title("METRICSTICS")

        # Initialize session ID
        self.session_id = None
        # Specify the directory path for session data
        current_directory = os.getcwd()
        
        # Specify the folder name
        folder_name = "SessionInfo"
        
        # Create the full path to the session directory
        self.session_directory = os.path.join(current_directory, folder_name)
        
        # Check if the directory exists, and create it if not
        if not os.path.exists(self.session_directory):
            os.makedirs(self.session_directory)
            print(f"Directory '{self.session_directory}' created.")

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
        visualize_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        self.export_data_button = ttk.Button(
            options_frame, text="Save Data", command=self.export_data_to_txt, width=25)
        self.export_data_button.grid(
            row=5, column=0, padx=5, pady=5, sticky="ew")

        label_data = ttk.Label(
            right_frame, text="Enter data (comma-separated):")
        label_data.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_data = tk.Text(right_frame, height=12, width=50)
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

        if self.load_latest_session_data():
            messagebox.showinfo(
                "Session Loaded", "Previous session data loaded successfully!")

        close_session_button = ttk.Button(
            options_frame, text="Close Session", command=self.close_session)
        close_session_button.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

        # Bind the close protocol to the custom function
        master.protocol("WM_DELETE_WINDOW", self.on_close_window)

    def generate_random_data(self):
        """Generate random data and fill the entry field."""
        # Prompt the user for the number of data points
        num_data_points = askinteger(
            "Generate Random Data", "Enter the number of data points (1-1000):", minvalue=1, maxvalue=1000)
        if num_data_points is None:
            # User clicked cancel
            return

        random_data = [round(random.uniform(0, 100), 2)
                       for _ in range(num_data_points)]
        self.entry_data.delete("1.0", tk.END)
        self.entry_data.insert(tk.END, ', '.join(map(str, random_data)))

    def calculate_statistics(self):
        """Calculate and display statistics based on user input."""
        selected_option = self.option_var.get()
        data = self.entry_data.get("1.0", tk.END)
        data = data.split(',')
        data = [float(x.strip()) for x in data if x.strip()]
        result = MetricsticsMain.calculate_metricstics(data, selected_option)
        if result != "Please enter valid data":
            self.export_button['state'] = 'normal'
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
        else:
            self.result_text.set(result)
            self.export_button['state'] = 'disabled'

    def export_to_csv(self, data_dict):
        """Export data to a CSV file."""
        self.result_text.set(MetricsticsMain.export_to_csv(data_dict))

    def clear_data(self):
        """Clear the data entry field."""
        self.entry_data.delete("1.0", tk.END)

    def show_help(self):
        """Display a help message."""
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
    7. Upload File:
        Upload a text file and populate the data

    Thank you for using METRICSTICS!"""

        help_label = ttk.Label(help_window, text=help_text,
                               wraplength=400, justify='left')
        help_label.pack(padx=20, pady=20)

        close_button = ttk.Button(
            help_window, text="Close", command=help_window.destroy)
        close_button.pack(pady=10)

    def upload_file(self):
        """Upload data from a file."""
        # Open a file dialog to choose a file
        file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=[("Text files", "*.txt")])

        # Read the content of the selected file and insert it into the entry_data Text widget
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.entry_data.delete("1.0", tk.END)
                self.entry_data.insert(tk.END, file_content)

    # Visualise Data

    def visualize_data(self):
        """Visualise data from the inputs."""
        data = self.entry_data.get("1.0", tk.END)
        data = data.split(',')
        data = [float(x.strip()) for x in data if x.strip()]

        self.plot_histogram(data)
        self.plot_box_plot(data)
        self.plot_line_chart(data)
        self.plot_scatter_plot(data)

    def plot_histogram(self, data):
        """Plot histogram from the data points"""
        plt.hist(data, bins=10, edgecolor='black')
        plt.title('Histogram')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

    def plot_box_plot(self, data):
        """Plot a boxplot from the data points"""
        plt.boxplot(data)
        plt.title('Box Plot')
        plt.xlabel('Data')
        plt.ylabel('Values')
        plt.show()

    def plot_line_chart(self, data):
        """Plot a line cahc plot from the data points"""
        x_values = list(range(1, len(data) + 1))
        plt.plot(x_values, data, marker='o')
        plt.title('Line Chart')
        plt.xlabel('Data Point')
        plt.ylabel('Value')
        plt.show()

    def plot_scatter_plot(self, data):
        """Plot a scatter plot for given data points"""
        x_values = list(range(1, len(data) + 1))
        plt.scatter(x_values, data)
        plt.title('Scatter Plot')
        plt.xlabel('Data Point')
        plt.ylabel('Value')
        plt.show()

# Export Data
    def export_data_to_txt(self):
        """Export data to txt file"""
        data = self.entry_data.get("1.0", tk.END).strip()
        if data:
            data_list = [float(x.strip())
                         for x in data.split(',') if x.strip()]

            # Create a text file with data
            filename = "exported_data.txt"
            with open(filename, mode='w') as file:
                file.write('\n'.join(map(str, data_list)))

            self.result_text.set(f"Data exported to {filename}")
        else:
            self.result_text.set("No data to export.")

    def load_latest_session_data(self):
        """Load latest session data"""
        try:
            latest_file = self.get_latest_session_file()
            if latest_file:
                with open(latest_file, 'r') as json_file:
                    data = json.load(json_file)
                    if 'Data' in data:
                        session_data = ', '.join(map(str, data['Data']))
                        self.entry_data.insert(tk.END, session_data)
                        return True
            return False
        except json.JSONDecodeError:
            messagebox.showwarning(
                "Invalid JSON", "Error loading session data. Invalid JSON format.")
            return False

    def get_latest_session_file(self):
        """Returns the latest session file"""
        # Get the latest session file based on creation time
        session_files = Path(self.session_directory).glob(
            "session_data_*.json")
        latest_file = max(session_files, key=os.path.getctime, default=None)
        return latest_file

    def on_close_window(self):
        """Close window behavior"""
        # Check if the session is already closed
        data_to_save = self.entry_data.get("1.0", tk.END).strip()
        if data_to_save:
            # If data is present, ask the user if they want to save before closing
            response = tk.messagebox.askyesno(
                "Unsaved Changes", "Do you want to save your changes before closing?")
            if response:
                self.close_session()
            else:
                # Delete session_data.json if the user clicks on "No"
                self.delete_session_data()
                self.master.destroy()
        else:
            # If no data, close the window directly
            self.master.destroy()

    def close_session(self):
        """Session closing behavior"""
        # Save data to a JSON file with a timestamp-based filename
        data_to_save = self.entry_data.get("1.0", tk.END).strip()
        if data_to_save:
            data_list = [float(x.strip())
                         for x in data_to_save.split(',') if x.strip()]
            session_id = self.get_session_id()
            with open(os.path.join(self.session_directory, f"session_data_{session_id}.json"), 'w') as json_file:
                json.dump({"Data": data_list}, json_file)

        # Clear data and close the window
        self.clear_data()
        self.master.destroy()

    def delete_session_data(self):
        """Delete session method"""
        # Delete session_data.json
        latest_file = self.get_latest_session_file()
        if latest_file:
            try:
                os.remove(latest_file)
            except FileNotFoundError:
                pass

    def get_session_id(self):
        """Returns the session ID associated with the current session"""
        # Generate a unique session ID using the uuid module
        return str(uuid.uuid4())
