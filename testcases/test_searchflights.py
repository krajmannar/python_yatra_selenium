# pytest --browser chrome --url https://www.yatra.com/
import time
import pytest
import softest

from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestsearchAndVerify(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @data(("New Delhi", "JFK", "25/03/2022", "1 Stop"), ("BLR", "MUC", "18/03/2022", "2 Stop"))
    @unpack
    def test_search_flights_1_stop(self, goingfrom, goingto, departuredate, stop):
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, departuredate)
        search_flight_result.filter_flights_by_stop(stop)
        allstops1 = search_flight_result.get_search_flight_results()
        self.ut.assertListItemText(allstops1, stop)


    # def test_search_flights_2_stop(self):
    #     search_flight_result = self.lp.searchFlights("New Delhi", "JFK", "12/03/2022")
    #     search_flight_result.filter_flights_by_stop("2 Stop")
    #     allstops1 = search_flight_result.get_search_flight_results()
    #     self.ut.assertListItemText(allstops1, "2 Stop")







