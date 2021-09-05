from selenium.webdriver.common.by import By
from pages.Basepage import Basepage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Resultpage(Basepage):

    flight_list = (By.CLASS_NAME, "lh1-5")
    book = (By.XPATH, "//span/input['Book']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_flights(self, return_val, to_val):
        x = self.get_element_text(self.flight_list)
        y = int(len(x) / 2)
        first_list= x[:y]
        second_list= x[y:]
        # y = x[2]
        # z = x[9]
        self.select_by_text(self.flight_list, first_list[to_val])
        self.select_by_text(self.flight_list, second_list[return_val])
        self.do_click(self.book)

