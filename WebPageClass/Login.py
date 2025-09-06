from selenium.webdriver.common.by import By


class LoginPage:

 username_name="username"
 email=""
 password_name="password"
 submit_btn_xpath="//button[@type='submit']"

 @staticmethod
 def enter_username(driver,un):
     username_ele=driver.find_element(By.NAME,LoginPage.username_name)
     username_ele.send_keys(un)

 @staticmethod
 def enter_password(driver,pwd):
    password_ele=driver.find_element(By.NAME,LoginPage.password_name)
    password_ele.send_keys(pwd)

 @staticmethod
 def click_sbtbtn(driver):
    sbt_btn=driver.find_element(By.XPATH,LoginPage.submit_btn_xpath)
    sbt_btn.click()
