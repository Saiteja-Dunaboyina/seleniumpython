from orangehrmhelper.selenium_actions import Selenium_Actions
from selenium.webdriver.common.by import By
import time

class AdminPage(Selenium_Actions):

    admin_button = (By.XPATH,"//span[text()='Admin']")
    add_button = (By.XPATH,"//button[text()=' Add ']")
    userrole_dropdown = (By.XPATH,"(//div[text()='-- Select --'])[1]")
    select_admin = (By.XPATH,"//div[@role='option']/span[text()='Admin']")
    empname_input = (By.XPATH,"//input[@placeholder='Type for hints...']")
    select_empname = (By.XPATH,"//div[@role='listbox']/div[1]")
    status_dropdown = (By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
    select_status = (By.XPATH,"//span[text()='Enabled']")
    username_input = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    password_input = (By.XPATH,"(//input[@type='password'])[1]")
    confirm_password_input = (By.XPATH,"(//input[@type='password'])[2]")
    save_button = (By.XPATH,"//button[text()=' Save ']")
    username_input2 = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    search_button = (By.XPATH,"//button[text()=' Search ']")
    delete_button = (By.XPATH,"//i[@class='oxd-icon bi-trash']")
    confirm_delete_button = (By.XPATH,"//button[text()=' Yes, Delete ']")

    def __init__(self,driver):
        super().__init__(driver)

    def add_employee(self,empname,username,password) :
        self.webelement_click(self.admin_button)
        self.webelement_click(self.add_button)
        self.webelement_click(self.userrole_dropdown)
        self.webelement_click(self.select_admin)
        self.webelement_input(self.empname_input,empname)
        time.sleep(5)
        self.webelement_click(self.select_empname)
        self.webelement_click(self.status_dropdown)
        self.webelement_click(self.select_status)
        self.webelement_input(self.username_input,username)
        self.webelement_input(self.password_input,password)
        self.webelement_input(self.confirm_password_input,password)
        self.webelement_click(self.save_button)
        time.sleep(5)

    def delete_employee(self,username) :
        self.webelement_click(self.admin_button)
        self.webelement_input(self.username_input2,username)
        self.webelement_click(self.search_button)
        self.webelement_click(self.delete_button)
        self.webelement_click(self.confirm_delete_button)