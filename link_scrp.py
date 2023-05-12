from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

link = "https://thehackernews.com/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    lnks = browser.find_elements(By.TAG_NAME, "a")
    for lnk in lnks:
        if "Hack" in lnk.text:
            answer = "Link text: " + lnk.get_attribute("href")
            print(answer)
finally:
    time.sleep(5)
    browser.quit()
    exit(0)
	
