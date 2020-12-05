from time import sleep
from selenium import webdriver
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class InstaBot:
    driver = None
    def __init__(self, username, pw, link, browser):
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
            self._share_post(driver)
        driver.quit()
    
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
