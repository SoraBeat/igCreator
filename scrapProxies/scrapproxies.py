from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from passwordgenerator import pwgenerator
from random_username.generate import generate_username
from fake_useragent import UserAgent
from latest_user_agents import get_random_user_agent
from names_dataset import NameDataset


import undetected_chromedriver as uc
import time
import pandas as pd
import random
import alphanum
import linecache
import names

protocol = "SOCKS5"
print("Starting...")
try:
    driver = uc.Chrome()
    driver.set_window_position(0, 0)
    driver.set_window_size(500, 500)

    driver.get("https://scrapingant.com/free-proxies/")
    time.sleep(5)
    
    rowsOfTheTable = driver.find_elements(
        By.XPATH, f"//table/tbody/tr[contains(.,'{protocol}')]")

    proxiesIFind = ""
    print("Proccess starting please wait...")
    for row in rowsOfTheTable:
        partsOfRow = row.text.split()
        proxiesIFind += partsOfRow[0]+":"+partsOfRow[1]+"\n"

    print("Finished! Check the proxies.txt file")
    fileTxt = open("../proxies.txt", "w")
    fileTxt.write(proxiesIFind)
    fileTxt.close()
    driver.close()
    driver.quit()
except NameError:
    print(NameError)
    print("Something go wrong, try again")
    driver.close()
    driver.quit()
