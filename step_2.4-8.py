from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from math import log, sin
import time


def math(x):
    return log(abs(12 * sin(x)))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    check = browser.find_element_by_id('price')
    wait = WebDriverWait(browser, 10)
    book = browser.find_element_by_id('book')
    element = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    if(element):
        book.click()
    input_value = browser.find_element_by_id("input_value")
    get_x = input_value.text
    res = math(int(get_x))
    inputVal = browser.find_element_by_id("answer")
    inputVal.send_keys(str(res))
    button = browser.find_element_by_id("solve")
    button.click() 

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
