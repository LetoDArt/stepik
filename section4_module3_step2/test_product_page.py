import time
from .pages.product_page import ProductPage


# link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'

def test_guest_can_go_to_login_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    time.sleep(5)
