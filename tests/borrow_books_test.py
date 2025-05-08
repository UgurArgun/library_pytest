import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from pages.borrow_books_page import BorrowBooksPage
from selenium.webdriver.support import expected_conditions as EC



def test_borrow_books_link(driver):
    assert BorrowBooksPage().borrow_books_link.is_displayed(), "Borrowing Books link is not visible"
    assert BorrowBooksPage().borrow_books_link.is_enabled(), "Borrowing Books link is not enabled"
    BorrowBooksPage().borrow_books_link.click()
    time.sleep(3)
    assert driver.current_url == "https://library1.cydeo.com/#borrowing-books", "URL is not correct"
    assert driver.title == "Library", "Page title is not correct"
    time.sleep(2)

def test_return_borrow_book(driver):
    assert BorrowBooksPage().borrow_books_link.is_displayed(), "Borrowing Books link is not visible"
    assert BorrowBooksPage().borrow_books_link.is_enabled(), "Borrowing Books link is not enabled"
    BorrowBooksPage().borrow_books_link.click()
    time.sleep(3)
    table = driver.find_element(By.ID, "borrowed_list")  # Your table locator

    rows = table.find_elements(By.TAG_NAME, "tr")

    expected_book_name = "Colobus guerza"
    expected_book_state = "NOT RETURNED"

    matching_row = None

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        # Check if second cell text matches target_text
        if len(cells) >= 6 and cells[1].text == expected_book_name and cells[5].text == expected_book_state:
            assert cells[4].text == "null", f"Expected 4th cell to be 'null', but got '{cells[5].text}'"
            matching_row = row
            break

    assert matching_row is not None, f"No row found with '{expected_book_name}' in second cell."

    # Find the <a> button in the first cell of the matching row
    first_cell = matching_row.find_element(By.TAG_NAME, "td")
    return_book_button = first_cell.find_element(By.TAG_NAME, "a")

    # Scroll into view (optional but recommended)
    driver.execute_script("arguments[0].scrollIntoView(true);", return_book_button)

    # Wait until clickable
    wait = WebDriverWait(driver, 10)
    clickable_button = wait.until(EC.element_to_be_clickable(return_book_button))

    # Click the button
    try:
        clickable_button.click()
    except Exception:
        # Fallback: use JavaScript click if normal click fails
        driver.execute_script("arguments[0].click();", clickable_button)

    # Optionally add assertions or waits here to verify the click had the expected effect
