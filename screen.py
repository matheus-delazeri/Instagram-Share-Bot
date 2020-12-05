from selenium import webdriver
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from instabot import InstaBot

class Screen:
    def __init__(self):
        window = Tk()
        window.geometry("300x350")
        window.resizable(0, 0)
        window.title("Instagram's Bot")

        label = Label(window, text="Username")
        label.place(x=50, y=50, anchor="center")
        label = Label(window, text="Password")
        label.place(x=50, y=100, anchor="center")
        label = Label(window, text="Link to post")
        label.place(x=50, y=150, anchor="center")
        label = Label(window, text="Select a browser")
        label.place(x=60, y=200, anchor="center")
        browser_list= ["Microsoft Edge","Opera","Google Chrome","Mozilla Firefox"]
        cbx = ttk.Combobox(window, values=browser_list, state="readonly", width=20)
        cbx.place(x=180, y=200, anchor="center")
        label = Label(window, text="*After hit the button the process\n will begin and the script will start to send\n the selected post to your first 6 suggested followers")
        label.config(width=100)
        label.place(x=150, y=250, anchor="center")

        user_text = StringVar()
        entry_user = Entry(window, textvariable=user_text)
        entry_user.place(x=150, y=50, anchor="center")
        pw_text = StringVar()
        entry_pw = Entry(window, textvariable=pw_text)
        entry_pw.place(x=150, y=100, anchor="center")
        link_text = StringVar()
        entry_link = Entry(window, textvariable=link_text)
        entry_link.place(x=150, y=150, anchor="center")
        
        myButton = Button(window, text="Start sharing", command= lambda: self.on_button_press(user_text, pw_text, link_text, cbx))
        myButton.place(x=150, y=300, anchor="center")

        window.mainloop()

    def on_button_press(self, username, password, link, combobox):
        user = username.get()
        pw = password.get()
        lk = link.get()
        cbx = combobox.get()
        InstaBot(user, pw, lk, cbx)