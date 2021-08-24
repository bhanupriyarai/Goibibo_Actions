from selenium.webdriver.common.by import By
from pages.Basepage import Basepage
import re


class Homepage(Basepage):

    flights: (By.XPATH, "//*[@class='active']")
    Round_trip_button: (By.ID, "roundTrip")
    From: (By.XPATH, "//*[@placeholder='From']")
    Destination: (By.XPATH, "//*[@placeholder='Destination']")
    Start_date_picker: (By.ID, "departureCalendar")
    calender_title: (By.CLASS_NAME, "DayPicker-Caption")
    Day: (By.CLASS_NAME,"DayPicker-Day")
    Nav_button: (By.CLASS_NAME, "DayPicker-NavButton DayPicker-NavButton--next")
    End_date_picker: (By.ID, "returnCalendar")
    Traveller_tab: (By.CLASS_NAME, "dF alignItemsCenter ico14 textOverflow blueGrey trvlr-box")
    Traveller_count: (By.ID, "adultPaxBox")
    traveller_type: (By.ID, "gi_class")
    Search_button: (By.XPATH, "//button[contains(text(),'SEARCH')]")

    def check_flights_selected(self):
        x = self.get_element_text(self.flights)
        y = re.search("Flights", x)
        print(" {0} is selected").format(y)

    def select_round_trip_option(self):
        self.do_click(self.Round_trip_button)

    def select_from_place(self, text):
        self.do_click(self.From)
        self.do_send_keys(self.From, text)
        self.select_by_text(self.From, text)

    def select_to_place(self, text):
        self.do_click(self.Destination)
        self.do_send_keys(self.Destination, text)
        self.select_by_text(self.Destination, text)

    def select_on_date(self, day, month, year):
        self.do_click(self.Start_date_picker)
        self.validate_date_picker(self.calender_title, month, year, self.Nav_button)
        self.select_by_text(self.Day, day)

    def select_return_date(self, day, month, year):
        self.do_click(self.End_date_picker)
        self.validate_date_picker(self.calender_title, month, year, self.Nav_button)
        self.select_by_text(self.Day, day)

    def select_num_traveller(self, num):
        self.do_click(self.Traveller_tab)
        self.do_send_keys(self.Traveller_count, num)

    def select_class_type(self, text):
        self.do_click(self.traveller_type)
        self.select_by_text(self.traveller_type, text)

    def search_flights(self):
        self.do_click(self.Search_button)

