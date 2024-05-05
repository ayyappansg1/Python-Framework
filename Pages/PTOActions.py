from faker import Faker
import faker.providers.address

from PageObjects.PTOPom import PTOPom
from utilities.baseclass import BaseClass


class PTOActions(PTOPom):
    def __init__(self, driver,url):
        self.faker = Faker()
        self.driver = driver
        self.url=url

    def click_add_policy_button(self):
        BaseClass.get_logger().info("Click add policy button")
        BaseClass.click_element(self.add_policy_button, self.driver)

    def createPTOPolicy(self):
        BaseClass.get_logger().info("Create PTO policy")
        BaseClass.click_element(self.timeoff_type_dropdown, self.driver)
        BaseClass.select_particular_dropdown_option(self.timeoff_type_dropdown_options, "Frequency Monthly",
                                                    self.driver)
        BaseClass.send_input_to_the_textBox(self.timeoff_type_name_text_box,
                                            self.faker.name(), self.driver)
        BaseClass.send_input_to_the_textBox(self.accrual_textbox, "0", self.driver)
        BaseClass.send_input_to_the_textBox(self.amount_textbox, "10", self.driver)
        BaseClass.click_element(self.save_button, self.driver)
        BaseClass.verify_element_present(self.add_policy_button,self.driver)
        BaseClass.click_element(self.profile_icon, self.driver)
        BaseClass.click_element(self.sign_out, self.driver)
        BaseClass.hard_refresh(self.driver,self.url)

