from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()
        self.solve_quiz_and_get_code()

        # bk_message = self.browser.find_element(*ProductPageLocators.SUCCESS_BOOK_MESSAGE)
        # bk = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        #
        # price_message = self.browser.find_element(*ProductPageLocators.SUCCESS_PRICE_MESSAGE)
        # price = self.browser.find_element(*ProductPageLocators.PRICE)

        # assert (bool(bk_message.text == bk.text) & bool(price_message.text == price.text)), True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should have disappeared, but it hasn't"

