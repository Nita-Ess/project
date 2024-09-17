import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connexion à la base de données MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="projetexamen"
    )

# Fonction de connexion
def login():
    user_login = login_entry.get()
    user_password = password_entry.get()
    
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE login = %s AND password = %s", (user_login, user_password))
    result = cursor.fetchone()
    
    if result:
        messagebox.showinfo("Success", "Login successful!")
        main_menu()
    else:
        messagebox.showerror("Error", "Invalid login or password.")
    
    cursor.close()
    db.close()

# Interface de connexion
root = tk.Tk()
root.title("Gestion des Bus - Connexion")

tk.Label(root, text="Login:").grid(row=0, column=0)
tk.Label(root, text="Password:").grid(row=1, column=0)

login_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

login_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
