from tkinter import *
from tkinter import messagebox
import json

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file=r"c:\Users\AnbeeRadhaiNandPush\OneDrive\Documents\Nandhalala\Python\projects\git\My-Projects\Password-manager\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

label=Label(text="Website:")
email=Label(text="Email/Username:")
password=Label(text="Password:")
label.grid(row=1,column=0)
email.grid(row=2,column=0)
password.grid(row=3,column=0)

website_entry=Entry(width=35)
email_entry=Entry(width=35)
password_entry=Entry(width=21)


website_entry.grid(row=1,column=1,columnspan=2)
email_entry.grid(row=2,column=1,columnspan=2)   
password_entry.grid(row=3,column=1)

password_entry.focus()
email_entry.focus()
website_entry.focus()

def generate_password():
    import random
    characters = "abcdefghijklmnopqrstuvwxyzA{BCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for i in range(12))
    password_entry.insert(0, password)
    
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website: {
            "email":email,
            "password":password
    }
              }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return
    else:
        try:
            with open("passwords.json", "r") as file:
                data=json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
    
    


gen_password_button=Button(text="Generate Password",command=generate_password)
gen_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
