from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json
def load_config(filename):
    with open(filename, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config
config = load_config('config.json')
# Initiate the browser

browser = webdriver.Chrome(ChromeDriverManager().install())
# Open the Website
browser.get(config["URL"])

# find elements
try: 
    email = browser.find_element(By.XPATH, "//input[contains(@name,'email')]")
    password = browser.find_element(By.XPATH, "//input[contains(@name,'password')]")
    address = browser.find_element(By.XPATH, "//input[contains(@name,'address')]")
    email.send_keys("abc@abc.pl")
    password.send_keys("sadsa")
    address.send_keys("sassa")
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "formsButton")))
    button.click()

except:
    print("Error")