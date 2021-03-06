import json
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox


def save():
    website = web_input.get()
    pwd = pwd_input.get()
    email = email_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd
        }
    }
    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please fill out all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            email_input.delete(0, END)
            pwd_input.delete(0, END)
            web_input.focus()


def search():
    print(f"Looking for {web_input.get()}")
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            result = data[web_input.get()]
            message = f"Email is {result['email']}\nPassword is {result['password']}"
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found")
    except KeyError:
        message = "No details found for this website"
    finally:
        messagebox.showinfo(title=f"{web_input.get()}", message=message)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.gif')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
web_input = Entry(width=30)
web_input.grid(row=1, column=1)
web_input.focus()

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=49)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "example@test.com")

pwd_label = Label(text="Password:")
pwd_label.grid(row=3, column=0)
pwd_input = Entry(width=30)
pwd_input.grid(row=3, column=1)

gen_button = Button(text="Generate Password", width=15)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
