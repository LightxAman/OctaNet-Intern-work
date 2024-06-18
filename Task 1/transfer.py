import tkinter as tk
from tkinter import messagebox


class Transfer:
    def __init__(self, app):
        self.app = app
        self.transfer_screen()

    def transfer_screen(self):
        tk.Label(self.app.main_frame, text="Enter recipient user ID").pack()
        to_user_id_entry = tk.Entry(self.app.main_frame)
        to_user_id_entry.pack()
        tk.Label(self.app.main_frame, text="Enter amount to transfer").pack()
        amount_entry = tk.Entry(self.app.main_frame)
        amount_entry.pack()
        tk.Button(self.app.main_frame, text="Transfer",
                  command=lambda: self.transfer(to_user_id_entry.get(), int(amount_entry.get()))).pack()
        tk.Button(self.app.main_frame, text="Back", command=self.app.main_menu).pack()

    def transfer(self, to_user_id, amount):
        if to_user_id in self.app.users:
            if amount <= self.app.users[self.app.current_user]["balance"]:
                self.app.users[self.app.current_user]["balance"] -= amount
                self.app.users[to_user_id]["balance"] += amount
                self.app.users[self.app.current_user]["transactions"].append(f"Transferred ${amount} to {to_user_id}")
                self.app.users[to_user_id]["transactions"].append(f"Received ${amount} from {self.app.current_user}")
                messagebox.showinfo("Success",
                                    f"Transferred ${amount} to {to_user_id}. New balance: ${self.app.users[self.app.current_user]['balance']}")
                self.app.main_menu()
            else:
                messagebox.showerror("Error", "Insufficient balance")
        else:
            messagebox.showerror("Error", "Recipient user ID not found")
