import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




class TestCorrectAnswer():

    browser = webdriver.Chrome()
    response_message = ""
    
    try: 
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        time.sleep(5)
        button = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
        button.click()

        input_login = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
        input_login.send_keys("yanchenkova.a@gmail.com")

        input_password = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        input_password.send_keys("Stefa-2014")

        submit = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        submit.click()

        time.sleep(10)

        required_input = browser.find_element(By.CSS_SELECTOR, "textarea")
        required_input.send_keys(str(math.log(int(time.time()))))

        
        button2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        button2.click()

        time.sleep(40)
        message_temp = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
        message = message_temp.text
        assert message=="Correct!", response_message.text(link + "is" + message) 
            
    finally:
        browser.quit()