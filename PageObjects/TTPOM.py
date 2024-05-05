from selenium.webdriver.common.by import By


class TTPom:
    add_policy_button = (By.XPATH, "//button[@data-testid='AddPolicy']")
    nameEditingPencilIcon = (
        By.XPATH, "//span[@data-testid='edit-policy-name']//*[local-name()='svg']/*[name()='path']")
    policyNameTextBox = (By.XPATH, "//input[@name='policyName']")
    assignToCountriesDropDown = (
        By.XPATH, "//span[text()='Assign to Countries']//following-sibling::span[text()='Please Select']")
    assignToCountriesDropDownOption = (
        By.XPATH, "(//span[text()='Assign to Countries']//following-sibling::div/div)[2]/span")
    assignToCustomerDropDown = (By.XPATH, "//span[text()='Customers']//following-sibling::span[text()='Please Select']")
    assignToCustomerDropDownOption = (By.XPATH, "(//span[text()='Customers']//following-sibling::div/div)[2]/span")
    multiEntryButton = (By.XPATH, "//span[text()='Multiple Daily Entry']")
    frequencyButton = (
        By.XPATH, "//label[contains(text(),'Time Tracking')]//following-sibling::div/span[text()='Monthly']")
    twiceAMonthOption = (By.XPATH, "//label[contains(text(),'Time Tracking')]//following-sibling::div/div/div/span")
    effectiveDate = (By.XPATH, "//input[@name='startDate']")
    saveButton = (By.XPATH, "//button[@type='submit']")
    check_loader = (By.XPATH, "//div[@class='loaderContainer']")
