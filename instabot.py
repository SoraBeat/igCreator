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
from random_word import RandomWords
from proxy_checking import ProxyChecker

import undetected_chromedriver as uc
import time
import pandas as pd
import random
import alphanum
import linecache
import names
import pyautogui
import os


def main():
    r = RandomWords()
    protocol = "socks5"
    while True:
        try:
            uc.TARGET_VERSION = random.randint(85, 100)
            fileproxy = open("./proxies.txt", "r")
            cantOfLines = len(fileproxy.readlines())
            proxy = linecache.getline(
                "proxies.txt", random.randint(1, cantOfLines))
            print((f'--proxy-server={protocol}://{proxy}'))
            checker = ProxyChecker()
            proxyRes = checker.check_proxy(proxy)
            if proxyRes["status"] == 1:
                print("Valid proxy! waiting 2 minutes to start")
                time.sleep(120)

                options = uc.ChromeOptions()
                options.add_argument('--ignore-ssl-errors=yes')
                options.add_argument('--ignore-certificate-errors')
                options.add_argument(f'--proxy-server={protocol}://{proxy}')

                options2 = uc.ChromeOptions()
                options2.add_argument('--ignore-ssl-errors=yes')
                options2.add_argument('--ignore-certificate-errors')
                options2.add_argument(f'--proxy-server={protocol}://{proxy}')

                driver = uc.Chrome(options=options)
                driver2 = uc.Chrome(options=options2)

                driver.set_window_position(0, 0)
                driver.set_window_size(500, 500)
                driver2.set_window_position(500, 0)
                driver2.set_window_size(500, 500)
                driver.set_page_load_timeout(20)
                driver2.set_page_load_timeout(20)

                driver.get("https://tempail.com/")
                driver2.get("https://www.instagram.com/accounts/emailsignup/")

                number = alphanum.generate(5)
                number2 = alphanum.generate(3)
                username = generate_username(1)[0]+number2
                fullName = names.get_last_name()+" "+number
                password = pwgenerator.generate()

                time.sleep(30)

                if driver.find_elements(By.XPATH, '//*[@id="cf-stage"]/div[6]/label/span') != []:
                    btnSkipCaptcha2 = driver.find_element(
                        By.XPATH, '//*[@id="cf-stage"]/div[6]/label/span')
                    driver.execute_script(
                        "arguments[0].click();", btnSkipCaptcha2)
                time.sleep(10)
                if driver.find_elements(By.XPATH, '//*[@id="challenge-stage"]/div/input') != []:
                    btnSkipCaptcha = driver.find_element(
                        By.XPATH, '//*[@id="challenge-stage"]/div/input')
                    driver.execute_script(
                        "arguments[0].click();", btnSkipCaptcha)
                time.sleep(30)

                txtEmailFake = driver.find_element(
                    By.XPATH, '//*[@id="eposta_adres"]')
                emailFake = txtEmailFake.get_attribute('value')

                txtPhoneNumber = driver2.find_element(By.NAME, 'emailOrPhone')
                txtPhoneNumber.send_keys(emailFake)
                time.sleep(5)
                txtFullName = driver2.find_element(By.NAME, 'fullName')
                txtFullName.send_keys(fullName)
                time.sleep(5)
                txtUserName = driver2.find_element(By.NAME, 'username')
                txtUserName.send_keys(username)
                time.sleep(5)
                txtPassword = driver2.find_element(By.NAME, 'password')
                txtPassword.send_keys(password)
                time.sleep(5)

                btnNextStepInsta = driver2.find_element(
                    By.XPATH, "//button[contains(., 'Registrarte')]")
                driver2.execute_script(
                    "arguments[0].click();", btnNextStepInsta)
                time.sleep(5)

                year = random.randint(1970, 2000)
                day = random.randint(1, 30)
                month = random.randint(1, 12)
                select = Select(driver2.find_element(
                    By.XPATH, '//*[@title="Año:"]'))
                select.select_by_value(str(year))
                time.sleep(5)
                select2 = Select(driver2.find_element(
                    By.XPATH, '//*[@title="Día:"]'))
                select2.select_by_value(str(day))
                time.sleep(5)
                select3 = Select(driver2.find_element(
                    By.XPATH, '//*[@title="Mes:"]'))
                select3.select_by_value(str(month))
                time.sleep(5)

                btnNextStepInsta2 = driver2.find_element(
                    By.XPATH, "//button[contains(., 'Siguiente')]")
                driver2.execute_script(
                    "arguments[0].click();", btnNextStepInsta2)
                time.sleep(5)
                if driver2.find_elements(By.XPATH, "//p[contains(., 'Espera unos minutos')]") != []:
                    raise Exception("El numero telefonico ya esta tomado")
                time.sleep(120)

                txtVerificationCode = driver.find_element(
                    By.XPATH, '/html/body/section[2]/div/div/div/ul/li[2]/a/div[3]')
                verificationCode = txtVerificationCode.text[:7].replace(
                    " ", "")
                time.sleep(5)

                txtConfirmationCode = driver2.find_element(
                    By.NAME, 'email_confirmation_code')
                txtConfirmationCode.send_keys(verificationCode)
                time.sleep(5)
                btnNextStepInsta3 = driver2.find_element(
                    By.XPATH, "//button[contains(., 'Siguiente')]")
                driver2.execute_script(
                    "arguments[0].click();", btnNextStepInsta3)

                if driver2.find_elements(By.XPATH, "//p[contains(., 'Puedes solicitar uno nuevo')]") != []:
                    raise Exception("El codigo no es valido")

                time.sleep(60)

                fileTxt = open("misLuchadores.txt", "a")
                fileTxt.write(emailFake+" "+password+"\n")
                fileTxt.close()

                print("Usuario creado exitosamente! "+username)

                # AGREGAR ACA BOTON EXTRA
                if driver2.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]") != []:
                    btnNoThanks = driver2.find_element(
                        By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                    driver2.execute_script(
                        "arguments[0].click();", btnNoThanks)
                    time.sleep(10)

                btnGoToProfile = driver2.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[6]/div/div/a')
                driver2.execute_script("arguments[0].click();", btnGoToProfile)
                time.sleep(10)

                btnGoToConfig = driver2.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/div/nav/div/header/div/div[1]/button')
                driver2.execute_script("arguments[0].click();", btnGoToConfig)
                time.sleep(10)

                btnGoToProfileSetting = driver2.find_element(
                    By.XPATH, "//a[contains(., 'Editar perfil')]")
                driver2.execute_script(
                    "arguments[0].click();", btnGoToProfileSetting)
                time.sleep(10)

                imageToSelect = "./images/" + str(random.randint(1, 50))+".jpg"

                btnLoadImage = driver2.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/article/div/div[1]/div/button')
                driver2.execute_script("arguments[0].click();", btnLoadImage)
                time.sleep(10)
                absolutePath = os.path.abspath(imageToSelect)
                pyautogui.write(absolutePath)
                time.sleep(10)
                pyautogui.press('enter')
                time.sleep(15)

                txtPresentation = driver2.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/article/form/div[4]/div/div/textarea')
                txtPresentation.send_keys(
                    r.get_random_word()+" "+r.get_random_word()+" "+r.get_random_word())

                time.sleep(10)

                btnSave = driver2.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/article/form/div[10]/div/div/button')
                driver2.execute_script("arguments[0].click();", btnSave)
                time.sleep(10)

                driver.close()
                driver.quit()
                driver2.close()
                driver2.quit()

            else:
                print("Error!, invalid proxy")

        except ValueError:
            print("something went wrong, retrying")
            print(ValueError)
            driver.close()
            driver.quit()
            driver2.close()
            driver2.quit()
        finally:
            driver.close()
            driver.quit()
            driver2.close()
            driver2.quit()


if __name__ == "__main__":
    for _ in range(1000):
        try:
            main()
            break
        except Exception as e:
            print(e)
            print('Restarting...')
