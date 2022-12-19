from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")

    SUCCESS_BOOK_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")

    SUCCESS_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")