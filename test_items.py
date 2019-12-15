import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_exists(browser):
    browser.get(link)
    #time.sleep(30)
    btn_add_to_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert btn_add_to_basket, 'Button "Add to basket" is not found'
    
    #assert btn_add_to_basket != None
    #try:
    #    browser.find_element_by_css_selector(".btn-add-to-basket")
    #except NoSuchElementException:
    #   pytest.fail('Button "Add to basket" is not found')


