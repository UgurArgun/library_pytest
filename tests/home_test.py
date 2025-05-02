import time
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_profile_name(driver):
    assert HomePage().user_profile_link.is_displayed()
    assert "Student" in HomePage().user_profile_link.text

@pytest.mark.smoke
def test_books_link(driver):
    assert HomePage().books_link.is_displayed()
    assert HomePage().books_link.is_enabled()

@pytest.mark.smoke
def test_book_categories(driver):
    assert HomePage().book_categories.is_displayed()
    book_categories_text = HomePage().book_categories.text
    assert book_categories_text == "Book Categories"
    assert HomePage().book_categories_dropdown.is_enabled()
    HomePage().book_categories_dropdown.click()
    actual_options = HomePage().get_all_dropdown_options()

    expected_options = [
        "ALL",
        "Action and Adventure",
        "Anthology",
        "Classic",
        "Comic and Graphic Novel",
        "Crime and Detective",
        "Drama",
        "Fable",
        "Fairy Tale",
        "Fan-Fiction",
        "Fantasy",
        "Historical Fiction",
        "Horror",
        "Science Fiction",
        "Biography/Autobiography",
        "Humor",
        "Romance",
        "Short Story",
        "Essay",
        "Memoir",
        "Poetry"
    ]

    assert actual_options == expected_options

    # Select "Poetry" option
    HomePage().select_option_by_text("Poetry")
    # Assert "Poetry" is selected

    selected_text = HomePage().get_selected_option_text()
    assert selected_text == "Poetry", f"Expected 'Poetry' to be selected but got '{selected_text}'"

    # Select "ALL" option
    HomePage().select_option_by_text("ALL")
    # Assert "ALL" is selected
    selected_text = HomePage().get_selected_option_text()
    assert selected_text == "ALL", f"Expected 'ALL' to be selected but got '{selected_text}'"

@pytest.mark.smoke
def test_search_input_box(driver):
    assert HomePage().search_input_box.is_displayed()
    assert HomePage().search_input_box.is_enabled()

    # Enter a search term that not exists
    HomePage().search_input_box.send_keys("Harry Potter")
    assert HomePage().search_input_box.get_attribute("value") == "Harry Potter"
    time.sleep(2)
    assert HomePage().no_entries_found_text.is_displayed()

    # Clear the search input box
    HomePage().search_input_box.clear()
    WebDriverWait(driver, 2)

@pytest.mark.smoke
def test_search_with_book_name(driver):
    # Enter a search term with book name and assert that the book is displayed
    HomePage().search_input_box.send_keys("His Dark Materials")
    time.sleep(3)
    assert HomePage().search_input_box.get_attribute("value") == "His Dark Materials"
    assert HomePage().no_entries_found_text.is_displayed()

    actual_texts = HomePage().get_all_cell_texts_from_odd_row()

    expected_texts = [
        "Borrow Book",
        "24848867",
        "His Dark Materials",
        "Ms. Tiesha Medhurst",
        "Classic",
        "1835",
        ""  # Borrowed by is empty for this book
    ]

    assert actual_texts == expected_texts, f"Expected {expected_texts} but got {actual_texts}"

    assert HomePage().borrow_book_button.is_enabled()
    assert EC.element_to_be_clickable(HomePage().borrow_book_button)

    # Clear the search input box
    HomePage().search_input_box.clear()
    time.sleep(3)

@pytest.mark.smoke
def test_search_with_author_name(driver):
    # Enter a search term with author name and assert that the book is displayed
    HomePage().search_input_box.send_keys("Ms. Tiesha Medhurst")
    sleep(2)
    assert HomePage().search_input_box.get_attribute("value") == "Ms. Tiesha Medhurst"

    actual_texts = HomePage().get_all_cell_texts_from_odd_row()

    expected_texts = [
        "Borrow Book",
        "24848867",
        "His Dark Materials",
        "Ms. Tiesha Medhurst",
        "Classic",
        "1835",
        ""  # Borrowed by is empty for this book
    ]

    assert actual_texts == expected_texts, f"Expected {expected_texts} but got {actual_texts}"

    expected_text = "Showing 1 to 1 of 1 entries"
    actual_text = HomePage().no_entries_found_text.text

    assert actual_text == expected_text, f"Expected text to be '{expected_text}' but got '{actual_text}'"

    assert HomePage().borrow_book_button.is_enabled()
    assert EC.element_to_be_clickable(HomePage().borrow_book_button)

@pytest.mark.smoke
def test_search_with_category_name(driver):
    # Enter a search term with category name and assert that the book is displayed
    HomePage().search_input_box.send_keys("Classic")
    time.sleep(5)
    assert HomePage().search_input_box.get_attribute("value") == "Classic"
    assert HomePage().no_entries_found_text.is_displayed()

    expected_text = "No entries found"
    actual_text = HomePage().no_entries_found_text.text

    assert actual_text == expected_text, f"Expected text to be '{expected_text}' but got '{actual_text}'"
