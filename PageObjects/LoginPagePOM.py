from selenium.webdriver.common.by import By


class LoginPagePOM:
    username = (By.XPATH, "//input[@type='email']")
    password = (By.XPATH, "//input[@type='password']")
    login_button = (By.XPATH, "//div[@class='login-from-submit']/button")

    def get_username_element(self):
        return LoginPagePOM.username

    def get_password_element(self):
        return LoginPagePOM.password

    def get_login_button_element(self):
        return LoginPagePOM.login_button

    # def send_username(self, usernametext):
    #     self.driver.find_element(*LoginPagePOM.username).send_keys(usernametext)
    #
    # def send_password(self, passwordtext):
    #     self.driver.find_element(*LoginPagePOM.password).send_keys(passwordtext)
    #
    # def click_login_button(self):
    #     self.driver.find_element(*LoginPagePOM.login_button).click()
