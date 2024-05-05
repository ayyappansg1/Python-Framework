from PageObjects.LoginPagePOM import LoginPagePOM


class LoginPageActions(LoginPagePOM):
    def __init__(self, driver):
        self.driver = driver


    def send_username(self,text):
        self.driver.find_element(*(self.get_username_element())).send_keys(text)

    def send_password(self,text):
        self.driver.find_element(*(self.get_password_element())).send_keys(text)

    def click_login_button(self):
        self.driver.find_element(*(self.get_login_button_element())).click()
