import pytest
from conftest import *
from orangehrmpages.loginpage import LoginPage
from orangehrmpages.adminpage import AdminPage

@pytest.mark.usefixtures("browser_setup","log_on_failure")
class Test_OrangeHrm:

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.loginpage = LoginPage(self.driver)
        self.adminpage = AdminPage(self.driver)

    def test_orangehrm_login(self,user_data):
        self.loginpage.login(user_data['Username'],user_data['Password'])
        assert True == self.loginpage.empname_is_displayed()
        self.loginpage.logout()

    def test_orangehrm_addemployee(self,user_data) :
        self.loginpage.login(user_data['Username'],user_data['Password'])
        self.adminpage.add_employee(user_data['emp_name'],user_data['emp_username'],user_data['emp_password'])
        self.loginpage.logout()

    def test_orangehrm_delete_employee(self,user_data):
        self.loginpage.login(user_data['Username'],user_data['Password'])
        self.adminpage.delete_employee(user_data['emp_username'])
        self.loginpage.logout()

    def teardown_class(self):
        self.driver.quit()
