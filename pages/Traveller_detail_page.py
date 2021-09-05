from selenium.webdriver.common.by import By
from pages.Basepage import Basepage


class Detailpage(Basepage):

    traveller_ele = (By.XPATH, "//span[contains(text(), 'TRAVELLER DETAILS')]")
    title_ = (By.CLASS_NAME, "lh1-5")
    first_name = (By.NAME, "givenname")
    last_name = (By.NAME, "lastname")
    email_id = (By.NAME, "email")
    number = (By.NAME, "mobile")
    proceed = (By.XPATH, "//button[contains(text(), 'Proceed')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_details(self, title, f_name, l_name, email, num):
        self.scroll_to(self.traveller_ele)
        self.select_by_text(self.title_, title)
        self.do_send_keys(self.first_name, f_name)
        self.do_send_keys(self.last_name, l_name)
        self.do_send_keys(self.email_id, email)
        self.do_send_keys(self.number, num)
        self.do_click(self.proceed)

