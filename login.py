# login panel

# module for handling database
import sqlite3

# import the modules we need, for creating a GUI...
from tkinter import Tk, messagebox, Button, Label, Entry, StringVar, PhotoImage

# import module to access system files
import os

# connecting to the database
conn = sqlite3.connect("Database.db")
c = conn.cursor()
try:
    c.execute('''CREATE TABLE database(email, username, password);''')
except:
    print('its already created')

# all variables
logingui = Tk()  # object of Tkinter for login
# varibles for signin
email_entry = StringVar()
username_entry = StringVar()
password_entry = StringVar()
# varibles for signup
emaile = StringVar()
usernamee = StringVar()
passworde = StringVar()
cpassword = StringVar()
# varibles to control block
forgotblock = 1
signupblock = 1

# all methods


# method of signin 
def signin():
    global email_entry
    global username_entry
    global password_entry
    emaile = email_entry
    usernamee = username_entry
    passworde = password_entry
    password = user = 0
    passwordcheck = c.execute(
        "SELECT password FROM database WHERE password='%s'" % passworde.get())
    passwordcheck = c.fetchall()
    if len(passwordcheck):
        password = 1
    usercheck = c.execute(
        "SELECT username FROM database WHERE username='%s'" % usernamee.get())
    if len(str(*usercheck)):
        user = 1
    # checking whether the email id and username exists in the database or not
    if len(passworde.get()) == 0 or len(usernamee.get()) == 0:
        messagebox.showwarning("Warning", "Fields cannot be left blank!!!")
    else:
        if password == 1 and user == 1:
            useragaincheck = c.execute(
                "SELECT username FROM database where password='%s'" % passworde.get())
            useragaincheck = c.fetchone()
            passwordagaincheck = c.execute(
                "SELECT password FROM database where username='%s'" % usernamee.get())
            passwordagaincheck = c.fetchone()
            if useragaincheck[0] == usernamee.get() and passwordagaincheck[0] == passworde.get():
                messagebox.showinfo(
                    "Let's Play!!!!!!", "Successfully Logged in!!!!")
                logingui.destroy()
            else:
                messagebox.showerror("Error", "Check Username or Password")
        else:
            messagebox.showerror("Error", "Check Username or Password")
    global forgotblock
    global signupblock
    forgotblock = 0
    signupblock = 0
    return


# method for signup
def make_id():
    global emaile
    global usernamee
    global passworde
    global cpassword

    b = conn.cursor()
    userexist = emailexist = 0
    emailvalidation = 1
    cursor = c.execute(
        "SELECT username FROM database where username = '%s'" % usernamee.get())
    if len(str(*cursor)):
        userexist = 1
    cursor1 = b.execute(
        "SELECT email FROM database where email = '%s'" % emaile.get())
    if len(str(*cursor1)):
        emailexist = 1
    domains = ['yahoo.com', 'gmail.com', 'hotmail.com', 'outlook.com']
    email = emaile.get()
    find = email.find('@')
    email = email[find + 1:]
    # checking the validation of an email id
    if email not in domains:
        messagebox.showerror("Games on Python", "Enter a valid Email Id")
        emailvalidation = 0
    if len(emaile.get()) == 0 or len(usernamee.get()) == 0:
        messagebox.showwarning("Warning", "Fields cannot be left blank!!!")
    else:
        if emailexist or userexist:
            messagebox.showwarning("Warning", "Email or Username exists")
        elif emailvalidation == 1 and cpassword.get() == passworde.get():
            messagebox.showinfo("Success", "User Created Successfully!!!")
            c.execute("INSERT INTO database VALUES ('%s','%s','%s')" %
                      (emaile.get(), usernamee.get(), passworde.get()))
            conn.commit()

    global forgotblock
    global signupblock
    forgotblockblock = 0
    signupblock = 0

    return


# method for forgot username
def forgot():
    global newusername_entry
    global newpassword_entry
    global confirmpassword

    usernamee = username_entry
    passworde = newpassword_entry
    cpassworde = confirmpassword

    b = conn.cursor()
    cursor = c.execute(
        "SELECT username FROM database where username ='%s'" % usernamee.get())
    cursor1 = b.execute(
        "SELECT password FROM database where password='%s'" % passworde.get())
    print(passworde.get(), usernamee.get(), cpassworde.get())
    if (len(usernamee.get()) == 0 or len(passworde.get()) == 0):
        messagebox.showwarning("Warning", "Fields cannot be left blank")
    else:
        if len(str(*cursor)):
            if len(str(*cursor1)) == 0:
                if cpassworde.get() == passworde.get():
                    c.execute("UPDATE database SET password ='%s' where username='%s'" % (
                        passworde.get(), usernamee.get()))
                    messagebox.showinfo(
                        "Games on Python", "Password Changed Successfully")
                    conn.commit()
                else:
                    messagebox.showerror("Games on Python", "Password doesn't match")
            else:
                messagebox.showerror("Games on Python", "Password or Username Exists")
        else:
            messagebox.showerror("Games on Python", "Username not found")
    return


def forgetdestroy():
    global forgotblock
    global signupblock
    forgotblock = 1
    signupblock = 0
    logingui.destroy()
    return


def signupdestroy():
    global forgotblock
    global signupblock
    forgotblock = 0
    signupblock = 1
    logingui.destroy()
    return


def again():
    signup.destroy()
    os.system("python3 combined.py")
    return


def again1():
    mforget.destroy()
    os.system("python3 combined.py")

# creation of login GUI
logingui.geometry("500x350+400+300")
logingui.title("Mini Games For Python")

# login Panel
image = PhotoImage(file=r"login.png")
Label(logingui, image=image).pack(side="right", padx=30, pady=50)
loginpanel = Label(
    logingui, text="Login Panel", font=("", 25)).place(x=145, y=10)

userlabel = Label(logingui, text="Username:", font=("", 15)).place(x=30, y=80)
userentry = Entry(logingui, textvariable=username_entry).place(
    x=140, y=83, width=200)

passwordlabel = Label(logingui, text="Password:", font=("", 15)).place(x=30, y=130)
passwordentry = Entry(logingui, textvariable=password_entry, show="*").place(
    x=140, y=133, width=200)

signinbutton = Button(
    logingui, text="SIGN IN", font=("", 10), command=signin).place(x=80, y=190)
signupbutton = Button(
    logingui, text="SIGN UP", font=("", 10), command=signupdestroy).place(x=250, y=190)

forgotlabel = Label(
    logingui, text="Forgot Username?", font=("", 8)).place(x=45, y=260)
forgotbutton = Button(logingui, text="CLICK HERE", font=(
    "", 8), command=forgetdestroy).place(x=150, y=255, width=100, height=25)

exitbutton = Button(text="EXIT", font=("", 8), command=exit).place(x=440, y=0)
logingui.mainloop()

# signup panel
if signupblock and forgotblock == 0:
    signup = Tk()
    signup.geometry("500x300+200+300")
    signup.title("Signup for Games")
    emaile = StringVar()
    usernamee = StringVar()
    passworde = StringVar()
    cpassword = StringVar()

    Label(signup, text="Email ID:", font=("", 12)).place(x=10, y=10)
    Entry(signup, textvariable=emaile).place(x=220, y=10)

    Label(signup, text="Username:", font=("", 12)).place(x=10, y=60)
    Entry(signup, textvariable=usernamee).place(x=220, y=60)

    Label(signup, text="Password:", font=("", 12)).place(x=10, y=110)
    Entry(signup, textvariable=passworde, show="*").place(x=220, y=110)

    Label(signup, text="Confirm Password:", font=("", 12)).place(x=10, y=160)
    Entry(signup, textvariable=cpassword, show="*").place(x=220, y=160)

    Button(signup, text="OK", font=("", 10), command=make_id).place(x=170, y=210)
    Button(signup, text="Click Here to login again", font=("", 10),
           command=again).place(x=110, y=250)
    signup.mainloop()



# forgot Panel
if forgotblock and signupblock == 0:  # check for the signup or signin button
    mforget = Tk()  # object of Tkinter module for forget panel
    username_entry = StringVar()
    newpassword_entry = StringVar()
    confirmpassword = StringVar()
    # creation of GUI
    mforget.geometry("475x200+400+200")
    mforget.title("Change Username")

    userlabel = Label(
        mforget, text="Enter your Username:", font=("", 12)).place(x=10, y=30)
    userentry = Entry(mforget, textvariable=username_entry).place(
        x=200, y=30, width=200)

    passlabel = Label(
        mforget, text="Enter new Password:", font=("", 12)).place(x=10, y=80)
    passentry = Entry(mforget, textvariable=newpassword_entry).place(
        x=200, y=80, width=200)

    cpasslabel = Label(
        mforget, text="Confirm Password:", font=("", 12)).place(x=10, y=130)
    cpassentry = Entry(mforget, textvariable=confirmpassword).place(
        x=200, y=130, width=200)

    forgetbutton = Button(mforget, text="OK", font=("", 10), command=forgot).place(
        x=100, y=160, width=50)
    exitbutton1 = Button(
        mforget, text="Exit", font=("", 8), command=exit).place(x=425, y=0)
    Button(mforget, text="Click Here to login again", font=("", 10),
           command=again1).place(x=160, y=160)
    global signupblock
    signupblock = 0
    mforget.mainloop()
