from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")

    SUCCESS_BOOK_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")

    SUCCESS_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators():
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right span a")

    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators():
    FORM_EMAIL = (By.ID, "id_registration-email")
    FORM_PASSWORD = (By.ID, "id_registration-password1")
    FORM_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

