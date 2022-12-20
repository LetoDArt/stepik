from .base_page import BasePage

from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        print('here')
        self.go_to_login_page()

        email_field = self.browser.find_element(*LoginPageLocators.FORM_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.FORM_PASSWORD)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.FORM_CONFIRM_PASSWORD)
        submit = self.browser.find_element(*LoginPageLocators.SUBMIT)

        email_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)

        submit.click()
