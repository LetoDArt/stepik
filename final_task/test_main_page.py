import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.main_basket
class TestCheckBasket():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, link)
        page.open()
        page.check_basket_for_guest_to_be_empty()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()