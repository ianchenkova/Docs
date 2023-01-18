from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    num = browser.find_element(By.ID, "input_value")
    value = num.text
    y = calc(value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # browser.execute_script("window.scrollBy(0, 100);")
    

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button.click()

finally:  
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # browser.execute_script("window.scrollBy(0, 100);")
button.click()