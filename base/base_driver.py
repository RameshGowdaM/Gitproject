import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        previous_height = self.driver.execute_script('return document.body.scrollHeight')

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            new_height = self.driver.execute_script('return document.body.scrollHeight')

            if new_height == previous_height:
                break

            previous_height = new_height

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_for_clickable_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        click_elements = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return click_elements

    def wait_for_visiblity_of_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        visible_elements = wait.until(EC.visibility_of_all_elements_located((locator_type, locator)))
        return visible_elements
