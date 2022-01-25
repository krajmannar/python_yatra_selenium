import time
import pytest
from pages.search_flight_result_page import SearchFlightResults
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class = 'viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value = 'Search Flights']"



    def getDepartFromField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepartureDateField(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return  self.wait_for_element_to_be_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        time.sleep(4)

        search_results = self.getGoingToResults()

        for results in search_results:
            if goingtolocation in results.text:
                print(results.text)
                results.click()
                time.sleep(4)
                break

    def enterDepartureDate(self, departuredate):
        self.getDepartureDateField().click()
        time.sleep(4)
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)

        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clickSearchFlightButton(self):
        self.getSearchButton().click()
        time.sleep(8)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightButton()
        search_flights_result = SearchFlightResults(self.driver)
        return search_flights_result




