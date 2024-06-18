import tkinter as tk
from tkinter import messagebox


def register_screen(app):
    tk.Label(app.main_frame, text="Register").pack()
    tk.Label(app.main_frame, text="User ID").pack()
    user_id_entry = tk.Entry(app.main_frame)
    user_id_entry.pack()
    tk.Label(app.main_frame, text="PIN").pack()
    pin_entry = tk.Entry(app.main_frame, show="*")
    pin_entry.pack()
    tk.Button(app.main_frame, text="Register",
              command=lambda: register(app, user_id_entry.get(), pin_entry.get())).pack()
    tk.Button(app.main_frame, text="Back to Login", command=app.login_screen).pack()


def register(app, user_id, pin):
    if user_id in app.users:
        messagebox.showerror("Error", "User ID already exists")
    else:
        app.users[user_id] = {"pin": pin, "balance": 0, "transactions": []}
        messagebox.showinfo("Success", "Registration successful")
        app.login_screen()


def login_screen(app):
    tk.Label(app.main_frame, text="Login").pack()
    tk.Label(app.main_frame, text="User ID").pack()
    user_id_entry = tk.Entry(app.main_frame)
    user_id_entry.pack()
    tk.Label(app.main_frame, text="PIN").pack()
    pin_entry = tk.Entry(app.main_frame, show="*")
    pin_entry.pack()
    tk.Button(app.main_frame, text="Login", command=lambda: login(app, user_id_entry.get(), pin_entry.get())).pack()
    tk.Button(app.main_frame, text="Register", command=app.register_screen).pack()


def login(app, user_id, pin):
    if user_id in app.users and app.users[user_id]["pin"] == pin:
        app.current_user = user_id
        app.main_menu()
    else:
        messagebox.showerror("Error", "Invalid User ID or PIN")
