import inspect
import logging
import time

import pytest
from selenium.common import ElementClickInterceptedException, TimeoutException, StaleElementReferenceException, \
    JavascriptException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    @staticmethod
    def click_element(element, driver):
        wait = WebDriverWait(driver, 30)
        try:
            wait.until(EC.element_to_be_clickable(element))
            BaseClass.get_logger().info("Click element using normal click")
            driver.find_element(*element).click()
        except ElementClickInterceptedException:
            BaseClass.get_logger().info("Clicked using Java script executor")
            try:
                driver.execute_script("arguments[0].click();", driver.find_element(*element))
            except JavascriptException:
                #wait.until(EC.invisibility_of_element_located(element))
                wait.until(EC.element_to_be_clickable(element))
                elements = driver.find_element(*element)
                actions = ActionChains(driver)
                actions.move_to_element(elements).click().perform()
        except StaleElementReferenceException:
            BaseClass.get_logger().info("inside stale element")
            driver.execute_script("arguments[0].click();", driver.find_element(*element))

    def send_key_with_clear_text(element_by, text, driver):
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located(element_by))
        element = driver.find_element(*element_by)
        #actions = ActionChains(driver)
        #actions.click(element).perform()
        driver.execute_script("arguments[0].value = '';", element)
        element.send_keys(text)

    @staticmethod
    def normalClick(element_by,driver):
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located(element_by))
        wait.until(EC.element_to_be_clickable(element_by))
        try:
            driver.find_element(*element_by).click()
        except ElementClickInterceptedException:
            BaseClass.click_element(element_by, driver)
        # except (NoSuchElementException | TimeoutException):
        #     BaseClass.get_logger().info("Error found on click Element.")
        #     wait.until(EC.visibility_of_element_located(element_by))
        #     wait.until(EC.element_to_be_clickable(element_by))
        #     driver.find_element(*element_by).click()
        # except ElementClickInterceptedException:
        #     BaseClass.click_element(element_by,driver)
    def scroll_into_view(element_by, driver):
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located(element_by))
        element = driver.find_element(*element_by)
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", element)
        wait.until(EC.element_to_be_clickable(element_by))

    def verify_element_present(element, driver):
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located(element))
        try:
            BaseClass.get_logger().info("Checking element is enabled or not")
            return driver.find_element(*element).is_enabled()
        except TimeoutException:
            return driver.find_element(*element).is_enabled()

    @staticmethod
    def send_input_to_the_textBox(element, text, driver):
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located(element))
        BaseClass.get_logger().info("Send input to the text Box")

        driver.find_element(*element).send_keys(text)

    @staticmethod
    def check_loader(element_by, driver):
        wait = WebDriverWait(driver, 30)
        try:
            return wait.until(EC.invisibility_of_element_located(element_by))
        except TimeoutException:
            wait2 = WebDriverWait(driver, 30 + 30)
            return wait2.until(EC.invisibility_of_element_located(element_by))
        except NoSuchElementException:
            return True

    @staticmethod
    def select_particular_dropdown_option(elements, text, driver):
        BaseClass.get_logger().info("Selecting particular dropdown value")
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located(elements))
        all_elements = driver.find_elements(*elements)
        for m in all_elements:
            if text in m.text:
                time.sleep(10)
                try:
                    m.click()
                except ElementClickInterceptedException:
                    BaseClass.get_logger().info(
                        "Inside element click intercepted exception.trying to click through java script")
                    driver.execute_script("arguments[0].click();", driver.find_element(m))
                break

    @staticmethod
    def hard_refresh(driver, url):
        BaseClass.get_logger().info("Hard Refresh")
        driver.refresh()
        driver.get(url)

    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("C://Users//ayyappan.g//PycharmProjects//Atlas_Pyton_Framework//sangar.log")
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
