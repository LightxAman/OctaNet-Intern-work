import tkinter as tk
from tkinter import messagebox


class Withdraw:
    def __init__(self, app):
        self.app = app
        self.withdraw_screen()

    def withdraw_screen(self):
        tk.Label(self.app.main_frame, text="Enter amount to withdraw").pack()
        amount_entry = tk.Entry(self.app.main_frame)
        amount_entry.pack()
        tk.Button(self.app.main_frame, text="Withdraw", command=lambda: self.withdraw(int(amount_entry.get()))).pack()
        tk.Button(self.app.main_frame, text="Back", command=self.app.main_menu).pack()

    def withdraw(self, amount):
        if amount > self.app.users[self.app.current_user]["balance"]:
            messagebox.showerror("Error", "Insufficient balance")
        else:
            self.app.users[self.app.current_user]["balance"] -= amount
            self.app.users[self.app.current_user]["transactions"].append(f"Withdrew ${amount}")
            messagebox.showinfo("Success",
                                f"Withdrew ${amount}. New balance: ${self.app.users[self.app.current_user]['balance']}")
            self.app.main_menu()
