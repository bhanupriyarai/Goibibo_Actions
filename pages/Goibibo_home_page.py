from selenium.webdriver.common.by import By
from pages.Basepage import Basepage
import re


class Homepage(Basepage):

    flights = (By.CLASS_NAME, "active")
    Round_trip_button = (By.ID, "roundTrip")
    From = (By.XPATH, "//input[@placeholder='From']")
    list_auto = (By.XPATH, "//li[contains(@id,'react-autosuggest-1-suggestion')]//div[@class='mainTxt clearfix']/span")
    Destination = (By.XPATH, "//input[@placeholder='Destination']")
    Start_date_picker = (By.ID, "departureCalendar")
    calender_title = (By.CLASS_NAME, "DayPicker-Caption")
    Day = (By.XPATH, "//div/div[@class='DayPicker-Day']")
    Nav_button = (By.XPATH, "//span[@aria-label='Next Month']")
    End_date_picker = (By.ID, "returnCalendar")
    Traveller_tab = (By.ID, "pax_link_common")
    Traveller_count = (By.ID, "adultPaxBox")
    traveller_type = (By.ID, "gi_class")
    Search_button = (By.XPATH, "//button[contains(text(),'SEARCH')]")

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver

    def check_flights_selected(self):
        x = self.get_element_text(self.flights)
        if "Flights" in x:
            print("flight is selected")

    def select_round_trip_option(self):
        self.do_click(self.Round_trip_button)

    def select_from_place(self, text):
        self.do_send_keys(self.From, text)
        self.select_by_text(self.list_auto, text)

    def select_to_place(self, text):
        self.do_send_keys(self.Destination, text)
        self.select_by_text(self.list_auto, text)

    def select_on_date(self, day, month):
        self.do_click(self.Start_date_picker)
        # self.validate_date_picker(self.calender_title, month)
        self.select_by_text(self.Day, day)

    def select_return_date(self, day, month):
        self.do_click(self.End_date_picker)
        # self.validate_date_picker(self.calender_title, month)
        self.select_by_text(self.Day, day)

    def select_num_traveller(self, num):
        self.do_click(self.Traveller_tab)
        self.do_send_keys(self.Traveller_count, num)

    def select_class_type(self, text):
        self.do_click(self.traveller_type)
        self.select_by_text(self.traveller_type, text)

    def search_flights(self):
        self.do_click(self.Search_button)


