from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def current_url(self, url):
        element = WebDriverWait(self.driver, 10).until(EC.url_contains(url))
        return bool(element)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def validate_date_picker(self, by_locator, month, year, next_button):
        month_year_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        Text_list = month_year_value.text
        month_val = Text_list.split(" ")[0].trim()
        year_val = Text_list.split(" ")[1].trim()
        while not (month_val == month and year_val == year):
            self.do_click(next_button)

    def get_element_text(self, by_locator):
        elements_text = []
        element_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for element in element_list:
            elements_text.append(element.text)
        return elements_text

    def select_by_text(self, by_locator, text):
        element_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for element in element_list:
            if element.text == text:
                element.click()
                break


    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

