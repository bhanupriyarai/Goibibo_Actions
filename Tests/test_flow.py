import time

from Tests.basetest import TestBase
from Config.raw import TestData
from pages.Goibibo_home_page import Homepage
from pages.Flight_search_result_page import Resultpage
from pages.Traveller_detail_page import Detailpage


class Test_flow(TestBase):

    def test_browser_setup(self):
        self.driver.get(TestData.Base_URL)
        self.driver.maximize_window()

    def test_validate_url(self):
        self.home = Homepage(self.driver)
        current = self.home.current_url(TestData.Base_URL)
        print("URL is correct")

    def test_check_flights_tab(self):
        self.home = Homepage(self.driver)
        self.home.check_flights_selected()

    def test_search_flights(self):
        self.home = Homepage(self.driver)
        self.home.select_round_trip_option()
        self.home.select_from_place(TestData.from_)
        self.home.select_to_place(TestData.To)
        self.home.select_on_date(TestData.from_day, TestData.from_month)
        self.home.select_return_date(TestData.return_day, TestData.from_month, TestData.from_year)
        self.home.select_num_traveller(TestData.num_traveller)
        self.home.select_class_type(TestData.type)
        self.home.search_flights()
        time.sleep(5)

    def test_select_flights(self):
        self.home = Resultpage(self.driver)
        self.home.select_flights(TestData.to_val, TestData.return_val)

    def test_select_traveller_details(self):
        self.home = Detailpage(self.driver)
        self.home.enter_details(TestData.title, TestData.first_name, TestData.last_name, TestData.email_id, TestData.number)
        time.sleep(10)




