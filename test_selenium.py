from time import *
from login import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(r"C:\Users\fkovacs\Downloads\chromedriver_win32\chromedriver.exe")


def navigation(driver):
    driver.find_element_by_xpath("//img[@alt='Vacs']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
    iframe = driver.find_element_by_css_selector("iframe")
    driver.switch_to.frame(iframe)
    driver.find_element_by_tag_name("a").click()
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a")))
    driver.find_element_by_xpath("//*[@class='button right nomargin']").click()
    select = Select(driver.find_element_by_name('make'))
    select.select_by_visible_text('Opel')
    print(select)


def main():
    login()
    navigation()


if __name__ == '__main__':
    main()
