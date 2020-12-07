from selenium import webdriver
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from instabot import InstaBot

class Screen:
    def __init__(self):
        window = Tk()
        window.geometry("300x400")
        window.resizable(0, 0)
        window.title("Instagram's Bot")

        label = Label(window, text="SHARE YOUR POST")
        label.place(x=150, y=30, anchor="center")
        label.config(font=(40))
        label = Label(window, text="Username")
        label.place(x=50, y=70, anchor="center")
        label = Label(window, text="Password")
        label.place(x=50, y=120, anchor="center")
        label = Label(window, text="Link to post")
        label.place(x=50, y=170, anchor="center")
        label = Label(window, text="Select a browser")
        label.place(x=60, y=220, anchor="center")
        browser_list= ["Microsoft Edge","Opera","Google Chrome","Mozilla Firefox"]
        cbx = ttk.Combobox(window, values=browser_list, state="readonly", width=20)
        cbx.place(x=180, y=220, anchor="center")
        label = Label(window, text="More delay?")
        label.place(x=60, y=250, anchor="center")
        delay_list= ["Yes","No"]
        cbx_delay = ttk.Combobox(window, values=delay_list, state="readonly", width=20)
        cbx_delay.place(x=180, y=250, anchor="center")
        label = Label(window, text="*After hit the button the process\n will begin and the script will start to send\n the selected post to your first 6 suggested followers")
        label.config(width=100)
        label.place(x=150, y=300, anchor="center")

        user_text = StringVar()
        entry_user = Entry(window, textvariable=user_text, width=30)
        entry_user.place(x=175, y=70, anchor="center")
        pw_text = StringVar()
        entry_pw = Entry(window, textvariable=pw_text, show="*", width=30)
        entry_pw.place(x=175, y=120, anchor="center")
        link_text = StringVar()
        entry_link = Entry(window, textvariable=link_text, width=30)
        entry_link.place(x=175, y=170, anchor="center")
        
        myButton = Button(window, text="Start sharing", command= lambda: self.on_button_press(user_text, pw_text, link_text, cbx, cbx_delay))
        myButton.place(x=150, y=350, anchor="center")

        window.mainloop()

    def on_button_press(self, username, password, link, combobox, combobox_delay):
        user = username.get()
        pw = password.get()
        lk = link.get()
        cbx = combobox.get()
        cbx_delay = combobox_delay.get()
        InstaBot(user, pw, lk, cbx, cbx_delay)