# sessions.py
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askinteger
from tkinter import filedialog


# sessions.py
class SessionManager:
    def __init__(self, sess_master):
        self.master = sess_master
        self.current_role = None

    def load_role_dropdown(self):
        roles = ["Student", "Professor", "Data Analyst",
                 "Data Scientist", "Researcher"]
        role_label = ttk.Label(self.master, text="Select your role:")
        role_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.role_dropdown = ttk.Combobox(
            self.master, values=roles, state="readonly", width=25)
        self.role_dropdown.grid(row=2, column=0, padx=5,
                                pady=(0, 10), sticky="ew")

        role_button = ttk.Button(
            self.master, text="Load Role", command=self.load_role)
        role_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        # self.master.geometry("700x400")

    def load_role(self):
        print("load_role method is being called.")  # Add this print statement
        self.current_role = self.role_dropdown.get()
        if not self.current_role:
            print("Please select a role.")
        else:
            self.master.title(f"METRICSTICS - {self.current_role}")
