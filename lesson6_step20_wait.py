from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


import math
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

"""
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
"""


try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser.get(link)


  good_price = browser.find_element(By.ID, "price").text

  

  # говорим Selenium проверять в течение 12 секунд, значение в выбранном локаторе не станет нужным
  WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
  
  button = browser.find_element(By.ID, "book")
  button.click()
  
  x = int(browser.find_element(By.ID, "input_value").text)
  y = calc(x)


  in1 = browser.find_element(By.ID, "answer")
  in1.send_keys(y)

  #button = browser.find_element(By.TAG_NAME, "button")

  button = browser.find_element(By.ID, "solve")
  button.click()
  

  time.sleep(10)


finally:
  browser.quit()



