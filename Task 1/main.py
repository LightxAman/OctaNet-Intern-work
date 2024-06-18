# By LightxAman

import tkinter as tk

from deposit import Deposit
from registration import register_screen, login_screen
from transactions import Transactions
from transfer import Transfer
from withdraw import Withdraw


class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")
        self.root.geometry("400x300")
        self.current_user = None
        self.users = self.load_users()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")

        self.login_screen()

    def load_users(self):
        # Here, load users from a file or database
        # For simplicity, using a dictionary
        try:
            with open("users.txt", "r") as file:
                users = eval(file.read())
        except FileNotFoundError:
            users = {}
        return users

    def save_users(self):
        with open("users.txt", "w") as file:
            file.write(str(self.users))

    def login_screen(self):
        self.clear_screen()
        login_screen(self)

    def register_screen(self):
        self.clear_screen()
        register_screen(self)

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.main_frame, text="Main Menu").pack()
        tk.Button(self.main_frame, text="Transaction History", command=self.transaction_history).pack()
        tk.Button(self.main_frame, text="Withdraw", command=self.withdraw_screen).pack()
        tk.Button(self.main_frame, text="Deposit", command=self.deposit_screen).pack()
        tk.Button(self.main_frame, text="Transfer", command=self.transfer_screen).pack()
        tk.Button(self.main_frame, text="Quit", command=self.quit).pack()

    def transaction_history(self):
        self.clear_screen()
        Transactions(self)

    def withdraw_screen(self):
        self.clear_screen()
        Withdraw(self)

    def deposit_screen(self):
        self.clear_screen()
        Deposit(self)

    def transfer_screen(self):
        self.clear_screen()
        Transfer(self)

    def quit(self):
        self.save_users()
        self.root.quit()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
