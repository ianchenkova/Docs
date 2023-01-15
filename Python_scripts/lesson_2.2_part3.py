from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1")
    value1 = num1.text

    num2 = browser.find_element(By.ID, "num2")
    value2 = num2.text

    sum = int(value1) + int(value2)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum)) # select.select_by_value("1"); select.select_by_visible_text("text");  select.select_by_index(index)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:  
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()