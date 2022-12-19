from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()
        self.solve_quiz_and_get_code()

        bk_message = self.browser.find_element(*ProductPageLocators.SUCCESS_BOOK_MESSAGE)
        bk = self.browser.find_element(*ProductPageLocators.BOOK_NAME)

        price_message = self.browser.find_element(*ProductPageLocators.SUCCESS_PRICE_MESSAGE)
        price = self.browser.find_element(*ProductPageLocators.PRICE)

        assert (bool(bk_message.text == bk.text) & bool(price_message.text == price.text)), True


