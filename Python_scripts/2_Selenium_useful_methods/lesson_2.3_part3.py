from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log((12*math.sin(int(x)))))  

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    num = browser.find_element(By.ID, "input_value")
    value = num.text
    y = calc(value)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



