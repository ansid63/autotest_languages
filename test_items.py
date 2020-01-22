link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time

def test_add_button_exist(browser):
    browser.get(link)

    time.sleep(5)

    browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert True, "There is no button here"