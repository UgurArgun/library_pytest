import time

from pages.borrow_books_page import BorrowBooksPage


def test_borrow_books_link(driver):
    assert BorrowBooksPage().borrow_books_link.is_displayed(), "Borrowing Books link is not visible"
    assert BorrowBooksPage().borrow_books_link.is_enabled(), "Borrowing Books link is not enabled"
    BorrowBooksPage().borrow_books_link.click()


