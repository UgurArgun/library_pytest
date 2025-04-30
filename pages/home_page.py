from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):
    BOOK_CATEGORIES_DROPDOWN = (By.ID, "book_categories")

    def __init__(self):
        super().__init__()
        self.user_profile_link = self.find_element(By.XPATH, "//a[@id='navbarDropdown']")
        self.books_link = self.find_element(By.XPATH, "//a[@href='#books']")
        self.book_categories = self.find_element(By.XPATH, "//label[@class='control-label col-md-4']")
        self.book_categories_dropdown = self.find_element(By.ID, "book_categories")

    def get_all_dropdown_options(self):
        super().__init__()
        self.dropdown = self.driver.find_element(*self.BOOK_CATEGORIES_DROPDOWN)
        self.select = Select(self.dropdown)
        return [option.text for option in self.select.options]

