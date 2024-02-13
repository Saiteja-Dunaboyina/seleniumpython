from orangehrmhelper.selenium_actions import Selenium_Actions
from selenium.webdriver.common.by import By

class LoginPage(Selenium_Actions):

    username_input = (By.XPATH,"//input[@placeholder='Username']")
    password_input = (By.XPATH,"//input[@placeholder='Password']")
    login_button = (By.XPATH,"//button[@type='submit']")
    empname_display = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    profile_pic = (By.XPATH,"//img[@class='oxd-userdropdown-img']")
    logout_button = (By.XPATH,"//a[text()='Logout']")

    def __init__(self,driver):
        super().__init__(driver)

    
    def login(self,username,password):
        self.webelement_input(self.username_input,username)
        self.webelement_input(self.password_input,password)
        self.webelement_click(self.login_button)

    def empname_is_displayed(self):
        return self.webelement_isdispalyed(self.empname_display)
    
    def logout(self):
        self.webelement_click(self.profile_pic)
        self.webelement_click(self.logout_button)

                        