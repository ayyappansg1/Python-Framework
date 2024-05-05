from selenium.webdriver.common.by import By


class PTOPom:
    add_policy_button = (By.XPATH, "//button[@data-testid='add-policy']")
    timeoff_type_dropdown = (By.XPATH, "//span[text()='Time Off Type']//following-sibling::span")
    timeoff_type_dropdown_options = (By.XPATH, "//span[@class='a-dropdown__option__item']")
    timeoff_type_name_text_box = (By.XPATH, "//input[@name='policyName']")
    accrual_textbox = (By.XPATH, "// input[ @ name = 'addTimeOffPolicyPlanModel.0.accrualStarts']")
    amount_textbox = (By.XPATH, "//input[@name='addTimeOffPolicyPlanModel.0.amount']")
    save_button = (By.XPATH, "//button[@data-testid='add-policy-btn']")
    profile_icon = (By.XPATH, "//button[contains(@class,'user-profile-img-button')]")
    sign_out = (By.XPATH, "//p[text()='Sign Out']")
