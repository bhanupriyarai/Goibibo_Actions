from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Basepage:

    Nav_button = (By.XPATH, "//span[@aria-label='Next Month']")

    def __init__(self, driver):
        self.driver = driver

    def current_url(self, url):
        element = WebDriverWait(self.driver, 10).until(EC.url_contains(url))
        return bool(element)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def validate_date_picker(self, by_locator, month):
        month_year_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        print(month_year_value)
        text_list = month_year_value.text
        print(text_list)
        month_val = text_list.split(" ")[0].strip()
        print(month_val)
        print(month)
        while not (month_val == month):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.Nav_button)).click()

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

    def scroll_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC._find_element(by_locator))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
