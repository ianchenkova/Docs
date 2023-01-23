import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestCorrectAnswer():

    @pytest.mark.parametrize("links", ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
    def test_correct_answer(self, browser, links):
        response_message = ""
        link = "{}".format(links)
        browser.get(link)
        button = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
        button.click()

        input_login = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
        input_login.send_keys("______")

        input_password = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        input_password.send_keys("______")

        submit = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        submit.click()

        required_input = browser.find_element(By.CSS_SELECTOR, "textarea")
        required_input.send_keys(str(math.log(int(time.time()))))

        wait = WebDriverWait(webdriver, 10)
        button2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        button2.click()

        
        message_temp = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
        message = message_temp.text

        
        assert message=="Correct!", response_message.text(link + "is" + message) 
            

    

    
