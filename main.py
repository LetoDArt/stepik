from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

link = "http://suninjuly.github.io/explicit_wait2.html"
current_dir = os.path.abspath(os.path.dirname(__file__))

def calc(x):
	return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # firstname = browser.find_element(By.NAME, 'firstname')
    # lastname = browser.find_element(By.NAME, 'lastname')
    # email = browser.find_element(By.NAME, 'email')
    # file = browser.find_element(By.NAME, 'file')
    #
    # firstname.send_keys('Leto')
    # lastname.send_keys('D-Art')
    # email.send_keys('vgon@sfedu.ru')
    # file.send_keys(os.path.join(current_dir, "dich.txt"))
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    send_button = browser.find_element(By.ID, "book")
    send_button.click()

    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    # confirm = browser.switch_to.alert
    # confirm.accept()
    #
    value = browser.find_element(By.ID, 'input_value')
    num = value.text

    res = calc(num)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(res)

    send_button = browser.find_element(By.ID, "solve")
    send_button.click()

finally:
    time.sleep(10)
    browser.quit()