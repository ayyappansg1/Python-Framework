from selenium.webdriver.common.by import By


class Dashboard_pom:
    settings_tab = (By.XPATH, "//span[text()='Settings']")
    manage_time_off = (By.XPATH, "//p[text()='Manage Time Off']")
    manage_time_tracking = (By.XPATH, "//p[text()='Manage Time Tracking']")

    def get_settings_tab(self):
        return Dashboard_pom.settings_tab

    def get_manage_timeoff(self):
        return Dashboard_pom.manage_time_off
    def get_manage_timeTracking(self):
        return Dashboard_pom.manage_time_tracking