from config import *
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\fkovacs\Downloads\chromedriver_win32\chromedriver.exe")


def login():
    driver.get ("http://admin.carusseldwt.com/sign")
    driver.find_element_by_name("username").send_keys(ADMIN_USERNAME)
    driver.find_element_by_name("password").send_keys("")
    driver.find_element_by_name("submit").click()
