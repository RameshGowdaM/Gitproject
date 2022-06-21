import time
import pytest
import softest

from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_log()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        # here we will mention all objects
        self.launch_page = LaunchPage(self.driver)
        self.ut = Utils()

    # """this is the 1 way of Data driven testing using DDT"""
    # @data(("Mumbai", "New York", "23/02/2022", "1 Stop"))
    # @unpack

    # """this is the 2 way of Data driven testing using json and yaml"""
    # @file_data("../testdata/test_data.json")

    # this (*) means that it is expecting that list data might come
    # """this is the 3 way of Data driven testing using Xlsx"""
    #@data(*Utils.read_data_from_excel("C:\\Users\\Hp\\PycharmProjects\\TestFrameworkMentor\\testdata\\test_excel_data.xlsx", "Sheet3"))

    @data(*Utils.read_data_from_csv("C:\\Users\\Hp\\PycharmProjects\\TestFrameworkMentor\\testdata\\test_csv_data.csv"))
    @unpack
    def test_search_flights_1_stop(self, going_from_origin, going_to_dest, going_depart_date, stop_filter):
        search_flight = self.launch_page.searchFlight(going_from_origin, going_to_dest, going_depart_date)
        # scrolling the page
        self.launch_page.page_scroll()
        search_flight.filter_flight_by_stop(stop_filter)
        all_stops = search_flight.get_search_flight_results()
        self.log.info(len(all_stops))
        self.ut.UtilitiesList(all_stops, stop_filter)

    # def test_search_flights_2_stop(self):
    #     seacrh_flight = self.launch_page.searchFlight("New Delhi", "New York", "12/02/2022")
    #     # scrolling the page
    #     self.launch_page.page_scroll()
    #     seacrh_flight.filter_flight_by_stop("2 Stop")
    #     all_stops = seacrh_flight.get_search_flight_results()
    #     print(len(all_stops))
    #     self.ut.UtilitiesList(all_stops, "2 Stop")
