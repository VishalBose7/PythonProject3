from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RSLogin:


 username_value = "//input[@name='username']"
 pwd_value = "//input[@name='password']"
 radiobtn = "//input[@value='user']"
 dropdown_xpath = "//select[@class='form-control']"
 check_box= "//input[@type='checkbox']"
 siginbtn = "//input[@id='signInBtn']"


 @staticmethod
 def enter_username(driver, un):
    usname = driver.find_element(By.XPATH, RSLogin.username_value)
    usname.send_keys(un)

 @staticmethod
 def enter_pwd(driver,p):
     pwd=driver.find_element(By.XPATH,RSLogin.pwd_value )
     pwd.send_keys(p)

 @staticmethod
 def select_radio(driver):
     rdbtn=driver.find_element(By.XPATH,RSLogin.radiobtn)
     rdbtn.click()

 @staticmethod
 def select_dropdown(driver,dd1):
     dd=driver.find_element(By.XPATH,RSLogin.dropdown_xpath)
     select_sd = Select(dd)
     select_sd.select_by_value(dd1)

 @staticmethod
 def select_checkbox(driver):
     chkbox=driver.find_element(By.XPATH,RSLogin.check_box)
     chkbox.click()

 @staticmethod
 def click_signin(driver):
     sgbtn=driver.find_element(By.XPATH,RSLogin.siginbtn)
     sgbtn.click()

