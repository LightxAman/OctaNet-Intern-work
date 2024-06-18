import tkinter as tk
from tkinter import messagebox

# Backend Storage
users = {
    "12345": {"pin": "1234", "balance": 1000, "transactions": []},
    "67890": {"pin": "5678", "balance": 2000, "transactions": []}
}

current_user = None

# ATM Operations
def login(user_id, pin):
    global current_user
    if user_id in users and users[user_id]["pin"] == pin:
        current_user = user_id
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid User ID or PIN")

def view_transactions():
    if current_user:
        transactions = users[current_user]["transactions"]
        transactions_str = "\n".join(transactions) if transactions else "No transactions yet."
        messagebox.showinfo("Transaction History", transactions_str)

def withdraw(amount):
    if current_user:
        balance = users[current_user]["balance"]
        if amount > balance:
            messagebox.showerror("Error", "Insufficient balance")
        else:
            users[current_user]["balance"] -= amount
            users[current_user]["transactions"].append(f"Withdrew ${amount}")
            messagebox.showinfo("Success", f"Withdrew ${amount}. New balance: ${users[current_user]['balance']}")

def deposit(amount):
    if current_user:
        users[current_user]["balance"] += amount
        users[current_user]["transactions"].append(f"Deposited ${amount}")
        messagebox.showinfo("Success", f"Deposited ${amount}. New balance: ${users[current_user]['balance']}")

def transfer(to_user_id, amount):
    if current_user:
        if to_user_id in users:
            if users[current_user]["balance"] >= amount:
                users[current_user]["balance"] -= amount
                users[to_user_id]["balance"] += amount
                users[current_user]["transactions"].append(f"Transferred ${amount} to {to_user_id}")
                users[to_user_id]["transactions"].append(f"Received ${amount} from {current_user}")
                messagebox.showinfo("Success", f"Transferred ${amount} to {to_user_id}. New balance: ${users[current_user]['balance']}")
            else:
                messagebox.showerror("Error", "Insufficient balance")
        else:
            messagebox.showerror("Error", "Recipient user ID not found")

def logout():
    global current_user
    current_user = None
    login_screen()

# GUI Functions
def login_screen():
    clear_screen()
    tk.Label(root, text="User ID").pack()
    user_id_entry = tk.Entry(root)
    user_id_entry.pack()
    tk.Label(root, text="PIN").pack()
    pin_entry = tk.Entry(root, show="*")
    pin_entry.pack()
    tk.Button(root, text="Login", command=lambda: login(user_id_entry.get(), pin_entry.get())).pack()

def main_menu():
    clear_screen()
    tk.Label(root, text="Main Menu").pack()
    tk.Button(root, text="Transaction History", command=view_transactions).pack()
    tk.Button(root, text="Withdraw", command=withdraw_screen).pack()
    tk.Button(root, text="Deposit", command=deposit_screen).pack()
    tk.Button(root, text="Transfer", command=transfer_screen).pack()
    tk.Button(root, text="Quit", command=logout).pack()

def withdraw_screen():
    clear_screen()
    tk.Label(root, text="Enter amount to withdraw").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack()
    tk.Button(root, text="Withdraw", command=lambda: withdraw(int(amount_entry.get()))).pack()
    tk.Button(root, text="Back", command=main_menu).pack()

def deposit_screen():
    clear_screen()
    tk.Label(root, text="Enter amount to deposit").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack()
    tk.Button(root, text="Deposit", command=lambda: deposit(int(amount_entry.get()))).pack()
    tk.Button(root, text="Back", command=main_menu).pack()

def transfer_screen():
    clear_screen()
    tk.Label(root, text="Enter recipient user ID").pack()
    to_user_id_entry = tk.Entry(root)
    to_user_id_entry.pack()
    tk.Label(root, text="Enter amount to transfer").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack()
    tk.Button(root, text="Transfer", command=lambda: transfer(to_user_id_entry.get(), int(amount_entry.get()))).pack()
    tk.Button(root, text="Back", command=main_menu).pack()

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Initialize GUI
root = tk.Tk()
root.title("ATM Interface")
root.geometry("300x200")
login_screen()
root.mainloop()
