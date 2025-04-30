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

