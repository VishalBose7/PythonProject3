from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import WebPageClass.Login
from WebPageClass.Login import LoginPage
from WebPageClass.rahulshetty_login import RSLogin


class TestExample1:
    def test_utkarsh(self):
        c = webdriver.ChromeOptions()
        c.add_argument("--incognito")
        driver = webdriver.Chrome(options=c)
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        sleep(5)
        RSLogin.enter_username(driver, "rahulshettyacademy")
        sleep(5)
        RSLogin.enter_pwd(driver, "learning")
        # RSLogin.select_radio(driver)
        sleep(5)
        RSLogin.select_dropdown(driver, "consult")
        sleep(5)
        RSLogin.select_checkbox(driver)
        RSLogin.click_signin(driver)
