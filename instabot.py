from time import sleep
from selenium import webdriver
from tkinter import *

class InstaBot:
    def __init__(self, username, pw, link):
        cont = 0
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('https://www.instagram.com')
        sleep(2)
        login_field = driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        pw_field = driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        btn_login = driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(7)
        driver.get(link)
        while():
            cont += 1
            self._share_post(driver)
    
    def _share_post(self, driver):
        btn_share = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/button")\
            .click()
        sleep(1)
        btn_direct = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div/div[1]")\
            .click()
        sleep(7)
        for x in range(2, 8):
            btn_contacts = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div[%i]/div/div[3]/button" % x)\
                .click()
            sleep(3)
        btn_send = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/div/button")\
            .click()
        print("Foto enviada com sucesso!")
        sleep(1)
class Screen:
    
    def __init__(self):
        window = Tk()
        window.geometry("250x250")
        label = Label(window, text="Username")
        label.place(x=50, y=50, anchor="center")
        label = Label(window, text="Password")
        label.place(x=50, y=100, anchor="center")
        label = Label(window, text="Link to post")
        label.place(x=50, y=150, anchor="center")

        user_text = StringVar()
        entry_user = Entry(window, textvariable=user_text)
        entry_user.place(x=150, y=50, anchor="center")
        pw_text = StringVar()
        entry_pw = Entry(window, textvariable=pw_text)
        entry_pw.place(x=150, y=100, anchor="center")
        link_text = StringVar()
        entry_link = Entry(window, textvariable=link_text)
        entry_link.place(x=150, y=150, anchor="center")
        
        myButton = Button(window, text="Start sharing", command= lambda: self.on_button_press(user_text, pw_text, link_text))
        myButton.place(x=125, y=220, anchor="center")

        window.mainloop()

    def on_button_press(self, username, password, link):
        user = username.get()
        pw = password.get()
        lk = link.get()
        InstaBot(user, pw, lk)

Screen()
