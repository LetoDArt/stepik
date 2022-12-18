import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def checker(link):
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
    first_name.send_keys('Leto')
    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
    last_name.send_keys('D-Art')
    email = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
    email.send_keys('vgon@sfedu.ru')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    time.sleep(5)
    browser.quit()

    return welcome_text


class MyTestCase(unittest.TestCase):
    result = "Congratulations! You have successfully registered!"
    def test_first(self):
        res = checker('http://suninjuly.github.io/registration1.html')
        self.assertEqual(self.result, res, 'Error')

    def test_second(self):
        res = checker('http://suninjuly.github.io/registration2.html')
        self.assertEqual(self.result, res, 'Error')



if __name__ == '__main__':
    unittest.main()
