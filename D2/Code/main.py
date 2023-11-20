import tkinter as tk
from gui import MetricsApp

if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()

    # Create an instance of the MetricsApp class (MetricsApp is a custom class in the 'gui' module)
    app = MetricsApp(root)

    # Start the Tkinter event loop
    root.mainloop()
