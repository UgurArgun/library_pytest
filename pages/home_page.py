from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    BOOK_CATEGORIES_DROPDOWN = (By.ID, "book_categories")
    ROW = (By.CSS_SELECTOR, "tr.odd[role='row']")

    def __init__(self):
        super().__init__()
        self.wait = WebDriverWait(self.driver, 10)  # explicit wait

    @property
    def book_categories(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@class='control-label col-md-4']")))

    @property
    def book_categories_dropdown(self):
        return self.wait.until(EC.presence_of_element_located(self.BOOK_CATEGORIES_DROPDOWN))

    @property
    def search_input_box(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))

    @property
    def no_entries_found_text(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='tbl_books_info']")))

    @property
    def borrow_book_button(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Borrow Book']")))

    def get_all_dropdown_options(self):
        select = Select(self.book_categories_dropdown)
        return [option.text for option in select.options]

    def select_option_by_text(self, text):
        select = Select(self.book_categories_dropdown)
        select.select_by_visible_text(text)

    def get_selected_option_text(self):
        select = Select(self.book_categories_dropdown)
        selected_option = select.first_selected_option
        return selected_option.text

    def get_all_cell_texts_from_row(self):
        row = self.wait.until(EC.presence_of_element_located(self.ROW))
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_texts = [cell.text.strip() for cell in cells]
        return cell_texts

    def select_option_by_text(self, text):
        dropdown = self.driver.find_element(*self.BOOK_CATEGORIES_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(text)

    def get_selected_option_text(self):
        dropdown = self.driver.find_element(*self.BOOK_CATEGORIES_DROPDOWN)
        select = Select(dropdown)
        selected_option = select.first_selected_option
        return selected_option.text

        # Locator for the specific row (adjust if needed)
    ROW_ODD = (By.CSS_SELECTOR, "tr.odd[role='row']")


    def disabled_borrow_book_button(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-primary btn-sm  disabled']")))
