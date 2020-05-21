from lib2to3.pgen2 import driver

from selenium import webdriver
from time import sleep
from login2 import site
from login2 import username
from login2 import pw
from webdriver_manager.chrome import ChromeDriverManager


class InstaBot:
    def __init__(self, site, username, pw):
        self.driver = webdriver.Chrome()
        self.site = site
        self.driver.get(site)
        self.driver.maximize_window()

        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/div[1]/div/a[3]') \
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[1]/fieldset/form/div[1]/div/input') \
           .send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[1]/fieldset/form/div[2]/div/div/input') \
            .send_keys(pw)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[1]/fieldset/form/div[4]/div/button')\
            .click()
        sleep(2)


my_bot = InstaBot(site, username, pw)
