import time
import pytest
# from builtins import len
from pages.search_flight_result_page import SearchFlightResults
from pages.yatra_launch_page import LaunchPage

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.utils import Utils
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestsearchAndVerify():
    def test_search_flights(self):

        lp = LaunchPage(self.driver)
        lp.enterDepartFromLocation("New Delhi")

        lp.enterGoingToLocation("New York")

        lp.enterDepartureDate("25/03/2022")
        lp.clickSearchFlightButton()

        sf = SearchFlightResults(self.driver)
        sf.filter_flights()

        allstops1 = sf.wait_for_presence_of_all_elements(By.XPATH, "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop')]")

        ut = Utils()
        ut.assertListItemText(allstops1, "1 Stop")









