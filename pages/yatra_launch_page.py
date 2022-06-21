import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from pages.search_flights_result_page import SearchFlightResults
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    Depart_from_field = "#BE_flight_origin_city"
    Going_to_field = "#BE_flight_arrival_city"
    Going_to_countries = ".viewport li "
    Select_departure_date = "//input[@id='BE_flight_origin_date']"
    All_Dates = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    Search_click_field = "//input[@value='Search Flights']"

    log = Utils.custom_log()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    def getDepartFromField(self):
        return self.wait_for_clickable_element(By.CSS_SELECTOR, self.Depart_from_field)

    def getGoingToField(self):
        return self.wait_for_clickable_element(By.CSS_SELECTOR, self.Going_to_field)

    def getGoingAllCountries(self):
        return self.wait_for_visiblity_of_elements(By.CSS_SELECTOR, self.Going_to_countries)

    def getDepartureDate(self):
        return self.wait_for_clickable_element(By.XPATH, self.Select_departure_date)

    def getAllDates(self):
        return self.wait_for_visiblity_of_elements(By.XPATH, self.All_Dates)

    def getSearchClickField(self):
        return self.driver.find_element(By.XPATH, self.Search_click_field)

    def enterdepartlocation(self, departlocation):
        time.sleep(2)
        self.getDepartFromField().click()
        time.sleep(2)
        self.getDepartFromField().send_keys(departlocation)
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)
        time.sleep(2)

    def entergoingtolocation(self, goingtolocation):
        self.getGoingToField().click()
        self.log.info("Clicked on going to .")
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        self.log.info("Typed text into going to field successfully.")
        time.sleep(2)
        countries = self.getGoingAllCountries()
        print((len(countries)))
        for country in countries:
            print(country.text)
            if goingtolocation in country.text:
                country.click()
                break

    def enterDepartureDate(self, departuredate):
        self.getDepartureDate().click()
        all_dates = self.getAllDates()
        # all_dates = self.driver.find_elements(By.XPATH, self.All_Dates)
        print(len(all_dates))
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                time.sleep(3)
                break

    def enterSearchField(self):
        self.getSearchClickField().click()
        time.sleep(4)

    def searchFlight(self, departlocation, goingtolocation, departuredate):
        self.enterdepartlocation(departlocation)
        self.entergoingtolocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.enterSearchField()
        search_flight = SearchFlightResults(self.driver)
        return search_flight
