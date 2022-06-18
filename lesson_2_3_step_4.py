from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name("btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    number_el = browser.find_element_by_id("input_value")
    number = number_el.text
    y = calc(int(number))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
