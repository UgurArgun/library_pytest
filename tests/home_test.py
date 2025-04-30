import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_profile_name(driver):
    assert HomePage().user_profile_link.is_displayed()
    assert "Student" in HomePage().user_profile_link.text


def test_books_link(driver):
    assert HomePage().books_link.is_displayed()
    assert HomePage().books_link.is_enabled()

def test_book_categories(driver):
    assert HomePage().book_categories.is_displayed()
    book_categories_text = HomePage().book_categories.text
    assert book_categories_text== "Book Categories"
    assert HomePage().book_categories_dropdown.is_enabled()
    HomePage().book_categories_dropdown.click()

