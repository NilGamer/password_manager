from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pwd_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = web_input.get()
    username = user_input.get()
    password = pwd_input.get()

    new_data = {website: {
        "email": username,
        "password": password,
    }}

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", mode='r') as file:
                # reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # saving the updated data
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            pwd_input.delete(0, END)

# ----------------------- Search Username ----------------------------#


def search_username():

    website = web_input.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

    else:
        if website in data.keys():
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Username: {email}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

web_label = Label(text="Website:", font=("Arial", 12))
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", font=("Arial", 12))
user_label.grid(column=0, row=2)

pwd_label = Label(text="Password:", font=("Arial", 12))
pwd_label.grid(column=0, row=3)

# Input

web_input = Entry(width=32)
web_input.focus()
web_input.grid(column=1, row=1)

user_input = Entry(width=50)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, 'email or username')

pwd_input = Entry(width=32)
pwd_input.grid(column=1, row=3)

# Buttons

search_button = Button(text="Search", command=search_username, width=14)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
