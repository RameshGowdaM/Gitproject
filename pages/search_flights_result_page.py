import logging
import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.utils import Utils


class SearchFlightResults(BaseDriver):
    Flight_filter_1_STOP = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    Flight_filter_2_STOP = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    Flight_filter_0_STOP = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULT = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or  contains(text(),'2 Stop')]"

    log = Utils.custom_log(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # self.wait = wait

    def get_filter_by_one_stop(self):
        return self.driver.find_element(By.XPATH, self.Flight_filter_1_STOP)

    def get_filter_by_two_stop(self):
        return self.driver.find_element(By.XPATH, self.Flight_filter_2_STOP)

    def get_filter_by_non_stop(self):
        return self.driver.find_element(By.XPATH, self.Flight_filter_0_STOP)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULT)

    def filter_flight_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop().click()
            self.log.warning("selected flights with 1 stop.")
            time.sleep(5)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop().click()
            self.log.warning("selected flights with 2 stop.")
            time.sleep(5)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop().click()
            self.log.warning("selected flights with Non stop.")
            time.sleep(5)
        else:
            self.log.warning("Please provide the valid filter option")
