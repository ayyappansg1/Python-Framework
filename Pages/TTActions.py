import time

from faker import Faker
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from PageObjects.TTPOM import TTPom
from utilities.baseclass import BaseClass


class TTActions(TTPom):
    def __init__(self, driver):
        self.driver = driver

    def fillTTDetails(self):
        BaseClass.get_logger().info("Create TT policy")
        faker = Faker()
        policyName = faker.first_name()+"UI"
        # time.sleep(10)
        BaseClass.check_loader(self.check_loader, self.driver)
        BaseClass.click_element(self.add_policy_button, self.driver)
        #BaseClass.click_element(self.nameEditingPencilIcon, self.driver)
        #try:
        BaseClass.normalClick(self.nameEditingPencilIcon, self.driver)
        #except ElementClickInterceptedException:
        #BaseClass.get_logger().info("Inside Element Click intercepted exception")
        #BaseClass.click_element(self.nameEditingPencilIcon, self.driver)

        BaseClass.send_key_with_clear_text(self.policyNameTextBox, policyName, self.driver)
        BaseClass.scroll_into_view(self.assignToCountriesDropDown, self.driver)
        BaseClass.click_element(self.assignToCountriesDropDown, self.driver)
        BaseClass.select_particular_dropdown_option(self.assignToCountriesDropDownOption, "Austria", self.driver);
        BaseClass.scroll_into_view(self.assignToCustomerDropDown, self.driver)
        BaseClass.click_element(self.assignToCustomerDropDown, self.driver)
        BaseClass.select_particular_dropdown_option(self.assignToCustomerDropDownOption, "Travelmate Limited",
                                                    self.driver)
        BaseClass.click_element(self.multiEntryButton, self.driver)
        BaseClass.scroll_into_view(self.frequencyButton, self.driver)
        BaseClass.click_element(self.frequencyButton, self.driver)
        BaseClass.select_particular_dropdown_option(self.twiceAMonthOption, "Twice A Month", self.driver)
        BaseClass.send_input_to_the_textBox(self.effectiveDate, "01/Oct/2023", self.driver)
        BaseClass.click_element(self.saveButton, self.driver)
