from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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


