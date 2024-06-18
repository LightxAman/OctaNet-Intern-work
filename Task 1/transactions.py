import tkinter as tk
from tkinter import messagebox


class Transactions:
    def __init__(self, app):
        self.app = app
        self.display_transactions()

    def display_transactions(self):
        tk.Label(self.app.main_frame, text="Transaction History").pack()
        transactions = self.app.users[self.app.current_user]["transactions"]
        transactions_str = "\n".join(transactions) if transactions else "No transactions yet."
        tk.Label(self.app.main_frame, text=transactions_str).pack()
        tk.Button(self.app.main_frame, text="Back", command=self.app.main_menu).pack()
