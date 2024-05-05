from PageObjects.DashboardPOM import Dashboard_pom
from utilities.baseclass import BaseClass


class DashboardActions(Dashboard_pom):
    def __init__(self, driver):
        self.driver = driver

    def click_settings(self):
        # self.driver.find_element(*(self.get_settings_tab())).click()
        BaseClass.click_element(self.get_settings_tab(), self.driver)

    def click_manage_timeoff(self):
        # self.driver.find_element(*(self.get_manage_timeoff())).click()
        BaseClass.click_element(self.get_manage_timeoff(), self.driver)

    def click_manage_time_tracking(self):
        # self.driver.find_element(*(self.get_manage_timeoff())).click()
        BaseClass.click_element(self.get_manage_timeTracking(), self.driver)
