# main.py
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from sessions import SessionManager
from gui import MetricsApp


class AppController:
    def __init__(self, master):
        self.master = master
        master.title("Session Manager")

        # Create a SessionManager instance
        self.session_manager = SessionManager(self.master)

        # Load role dropdown in the main window
        self.session_manager.load_role_dropdown()

        # Add a button to proceed to the MetricsApp
        proceed_button = ttk.Button(
            master, text="Proceed to MetricsApp", command=self.open_metrics_app)
        proceed_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

    def open_metrics_app(self):
        # Retrieve the current role before creating MetricsApp instance
        current_role = self.session_manager.current_role
        print(f"Current role before creating MetricsApp: {current_role}")

        # Create MetricsApp instance and pass the current_role
        self.metrics_app = MetricsApp(self.master, current_role)

        # self.master.geometry("700x400")


if __name__ == "__main__":
    root = tk.Tk()
    app_controller = AppController(root)

    # Set the role from the dropdown selection
    selected_role = app_controller.session_manager.current_role

    # Check if a role is selected before proceeding to MetricsApp
    if selected_role:
        app_controller.open_metrics_app()
    else:
        print("Please select a role.")

    root.mainloop()
