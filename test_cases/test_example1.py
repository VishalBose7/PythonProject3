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

    def test_test1(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(5)
        LoginPage.enter_username(driver,"Admin")
        LoginPage.enter_password(driver,"admin123")
        LoginPage.click_sbtbtn(driver)
        sleep(5)
        driver.quit()

    def test_utkarsh(self):
        c = webdriver.ChromeOptions()
        c.add_argument("--incognito")
        driver = webdriver.Chrome(options=c)
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        RSLogin.enter_username(driver, "rahulshettyacademy")
        RSLogin.enter_pwd(driver, "learning")
        RSLogin.select_radio(driver)
        sleep(5)
        RSLogin.select_dropdown(driver, "Consultant")
        RSLogin.select_checkbox(driver)
        RSLogin.click_signin(driver)




    def test_test2(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(5)
        LoginPage.enter_username(driver, "Vishal")
        LoginPage.enter_password(driver, "admin123")
        LoginPage.click_sbtbtn(driver)
        sleep(5)
        driver.quit()

    def test_test3(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(5)
        LoginPage.enter_username(driver, "Admin1223")
        LoginPage.enter_password(driver, "admin123")
        LoginPage.click_sbtbtn(driver)
        sleep(5)
        driver.quit()