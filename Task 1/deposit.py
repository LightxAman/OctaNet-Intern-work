import tkinter as tk
from tkinter import messagebox


class Deposit:
    def __init__(self, app):
        self.app = app
        self.deposit_screen()

    def deposit_screen(self):
        tk.Label(self.app.main_frame, text="Enter amount to deposit").pack()
        amount_entry = tk.Entry(self.app.main_frame)
        amount_entry.pack()
        tk.Button(self.app.main_frame, text="Deposit", command=lambda: self.deposit(int(amount_entry.get()))).pack()
        tk.Button(self.app.main_frame, text="Back", command=self.app.main_menu).pack()

    def deposit(self, amount):
        self.app.users[self.app.current_user]["balance"] += amount
        self.app.users[self.app.current_user]["transactions"].append(f"Deposited ${amount}")
        messagebox.showinfo("Success",
                            f"Deposited ${amount}. New balance: ${self.app.users[self.app.current_user]['balance']}")
        self.app.main_menu()
