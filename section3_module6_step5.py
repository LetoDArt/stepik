import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


LOGIN = 'vgon@sfedu.ru'
PASSWORD = 'Havaysnikersy110399'
def answer_former(value):
    return math.log(int(value))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestTask:
    def test_stepik(self, browser, id):
        link_login = f'https://stepik.org/'
        browser.implicitly_wait(15)
        browser.get(link_login)

        answer = answer_former(time.time())

        data_tab = browser.find_element(By.CLASS_NAME, 'navbar__auth_login')
        data_tab.click()

        login = browser.find_element(By.ID, 'id_login_email')
        login.send_keys(LOGIN)
        password = browser.find_element(By.ID, 'id_login_password')
        password.send_keys(PASSWORD)
        log_btn = browser.find_element(By.CLASS_NAME, 'sign-form__btn')
        log_btn.click()

        time.sleep(2)

        link = f'https://stepik.org/lesson/{id}/step/1'
        browser.get(link)

        time.sleep(5)

        text_area = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ember-text-area'))
        )
        text_area.send_keys(answer)

        button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'submit-submission'))
        )
        time.sleep(1)
        button.click()

        res = WebDriverWait(browser, 7).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        )
        value = res.text

        assert 'Correct!' == value
