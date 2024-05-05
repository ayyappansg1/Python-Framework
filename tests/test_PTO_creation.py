import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.LoginPagePOM import LoginPagePOM
from Pages.DashboardActions import DashboardActions
from Pages.LoginPageActions import LoginPageActions
from Pages.PTOActions import PTOActions
from Pages.TTActions import TTActions
from testData.testData import TestData
from utilities.baseclass import BaseClass


# from utilities.base_class import BaseClass

class TestOne(BaseClass):

    def test_PTO_Policy_creation(self, newExcelData):
        loginPage = LoginPageActions(self.driver)
        loginPage.send_username(newExcelData["username"])
        loginPage.send_password(newExcelData["password"])
        loginPage.click_login_button()
        dashboard_actions = DashboardActions(self.driver)
        dashboard_actions.click_settings()
        dashboard_actions.click_manage_timeoff()
        pto_actions = PTOActions(self.driver, self.url)
        pto_actions.click_add_policy_button()
        pto_actions.createPTOPolicy()
        # self.send_input_to_the_textBox(LoginPagePOM.username, )
        # self.send_input_to_the_textBox(LoginPagePOM.password, "Atlas@123")
        # self.click_element(LoginPagePOM.login_button)

        # loginPage.click_login_button()
        # self.driver.find_element(By.XPATH,"//input[@type='email']").send_keys("customerhronly@yopmail.com")
        # self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Atlas@123")
        # self.driver.find_element(By.XPATH,"//div[@class='login-from-submit']/button").click()
        # time.sleep(5)

    def test_TT_Policy_creation(self,testDataSuperAdmin):
        loginPage = LoginPageActions(self.driver)
        loginPage.send_username(testDataSuperAdmin["username"])
        loginPage.send_password(testDataSuperAdmin["password"])
        loginPage.click_login_button()
        dashboard_actions = DashboardActions(self.driver)
        dashboard_actions.click_settings()
        dashboard_actions.click_manage_time_tracking()
        ttActions=TTActions(self.driver)
        ttActions.fillTTDetails()



@pytest.fixture(params=TestData.getExcelData("QA"))
def credentials(request):
    return request.param

@pytest.fixture(params=TestData.test_data_superAdmin)
def testDataSuperAdmin(request):
    return request.param

@pytest.fixture(params=TestData.getExcelData("AnotherQA"))
def credentialsAnother(request):
    return request.param

@pytest.fixture(params=TestData.getExcelDataTrail())
def newExcelData(request):
    return request.param