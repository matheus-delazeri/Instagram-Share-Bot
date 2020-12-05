from time import sleep
from selenium import webdriver
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class InstaBot:
    driver = None
    def __init__(self, username, pw, link, browser):
        cont = 0
        driver = self._get_browser(browser)
        driver.get('https://www.instagram.com')
        sleep(3)
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

    def _get_browser(self, browser):
        cont = 0
        if(browser == 'Microsoft Edge'):
            for x in range(1, 4):
                try:
                    driver = webdriver.Edge('browser_drivers/msedgedriver_{}.exe'.format(x))
                except:
                    cont += 1
                    print("Wrong version")
        elif(browser == 'Opera'):
            for x in range(1, 4):
                try:
                    driver = webdriver.Opera('browser_drivers/operadriver_{}.exe'.format(x))
                except:
                    cont += 1
                    print("Wrong version")
        elif(browser == 'Google Chrome'):
            for x in range(1, 4):
                try:
                    driver = webdriver.Chrome('browser_drivers/chromedriver_{}.exe'.format(x))
                except:
                    cont += 1
                    print("Wrong version")
        elif(browser == 'Mozilla Firefox'):
            for x in range(1, 4):
                try:
                    driver = webdriver.Firefox('browser_drivers/geckodriver_{}.exe'.format(x))
                except:
                    print("Wrong version")
                    cont += 1
        else:
            messagebox.showwarning(title="Error", message="Select a browser!")
        
        if(cont == 3):
             messagebox.showwarning(title="Error", message="It seems you don't have this browser intalled! Please select another one")
        else:
            return driver        

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
