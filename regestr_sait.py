from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.clientam.com/sso/Login"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "user_name")
    input1.send_keys("admin")
    input2 = browser.find_element(By.ID, "password")
    input2.send_keys("admin")
    button = browser.find_element(By.ID, "submitForm")
    button.click()

    time.sleep(20)
    invalid = browser.find_element(By.ID, "ERRORMSG")
    invalid_text = invalid.text

    print(invalid_text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
