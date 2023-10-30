import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import csv

def generate_random_data():
    num_data_points = random.randint(5, 20)
    random_data = [round(random.uniform(0, 100), 2) for _ in range(num_data_points)]
    entry_data.delete("1.0", tk.END)  
    entry_data.insert(tk.END, ', '.join(map(str, random_data)))  

def calculate_statistics():
    global selected_option  
    selected_option = option_var.get()
    data = entry_data.get("1.0", tk.END)
    data = data.split(',')
    data = [float(x.strip()) for x in data if x.strip()]
    
    if not data:
        result_text.set("Please enter valid data")
        return

    n = len(data)
    
    if selected_option == "Minimum":
        result_text.set(f"Minimum: {min(data)}")
    elif selected_option == "Maximum":
        result_text.set(f"Maximum: {max(data)}")
    elif selected_option == "Mode":
        frequency = {}
        for item in data:
            frequency[item] = frequency.get(item, 0) + 1
        mode = max(frequency, key=frequency.get)
        result_text.set(f"Mode: {mode}")
    elif selected_option == "Median":
        sorted_data = sorted(data)
        if n % 2 == 1:
            median = sorted_data[n // 2]
        else:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        result_text.set(f"Median: {median}")
    elif selected_option == "Mean":
        mean = sum(data) / n
        result_text.set(f"Mean: {mean}")
    elif selected_option == "Mean Absolute Deviation":
        mean = sum(data) / n
        mad = sum(abs(x - mean) for x in data) / n
        result_text.set(f"Mean Absolute Deviation: {mad}")
        export_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        export_data = {"Data": data, "Mean Absolute Deviation": [mad]}
        export_button.config(command=lambda: export_to_csv(export_data))
    elif selected_option == "Standard Deviation":
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = variance ** 0.5
        result_text.set(f"Standard Deviation: {std_dev}")
        export_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        export_data = {"Data": data, "Statistic": selected_option}
        export_button.config(command=lambda: export_to_csv(export_data))

def export_to_csv(data_dict):
    filename = "statistics_data.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Data'])
        for value in data_dict['Data']:
            writer.writerow([value])
        if 'Mean Absolute Deviation' in data_dict:
            writer.writerow(['MAD =', data_dict['Mean Absolute Deviation']])
        elif 'Standard Deviation' in data_dict:
            writer.writerow(['SD =', data_dict['Standard Deviation']])
    result_text.set(f"Data exported to {filename}")

def clear_data():
    entry_data.delete("1.0", tk.END)

def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    
    help_text = """
    This section need to be updated after discussion
    """
    
    help_label = ttk.Label(help_window, text=help_text, wraplength=400, justify='left')
    help_label.pack(padx=20, pady=20)
    
    close_button = ttk.Button(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)

root = tk.Tk()
root.title("METRICSTICS")

style = ttk.Style()
style.configure('TButton', borderwidth=2, relief="groove", foreground="black")

options_frame = tk.Frame(root)
options_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

options_label = ttk.Label(options_frame, text="Options:")
options_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

options = ["Minimum", "Maximum", "Mode", "Median", "Mean", "Mean Absolute Deviation", "Standard Deviation"]
option_var = tk.StringVar(value=options[0])
option_menu = ttk.OptionMenu(options_frame, option_var, *options)
option_menu.config(width=25)  
option_menu.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")

random_data_button = ttk.Button(options_frame, text="Generate Random Data", command=generate_random_data, width=25)
random_data_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

label_data = ttk.Label(right_frame, text="Enter data (comma-separated):")
label_data.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_data = tk.Text(right_frame, height=5, width=50)
entry_data.grid(row=1, column=0, padx=5, pady=5)

bottom_frame = tk.Frame(root)
bottom_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="s")

calculate_button = ttk.Button(bottom_frame, text="Calculate Statistics", command=calculate_statistics)
calculate_button.grid(row=0, column=0, padx=5, pady=5)

clear_button = ttk.Button(bottom_frame, text="Clear Data", command=clear_data)
clear_button.grid(row=0, column=1, padx=5, pady=5)

result_text = tk.StringVar()
result_label = ttk.Label(bottom_frame, textvariable=result_text)
result_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

help_icon = tk.PhotoImage(file="help.png")
help_button = ttk.Button(root, image=help_icon, style='IconButton.TButton')
help_button.grid(row=0, column=1, sticky="ne")

style.configure('IconButton.TButton', borderwidth=0)
help_button.bind("<Button-1>", lambda e: show_help())

export_button = ttk.Button(bottom_frame, text="Export to CSV")
export_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
export_button.grid_remove()  

root.mainloop()
