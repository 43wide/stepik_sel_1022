from selenium import webdriver
from selenium.webdriver.common.by import By
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
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser.get(link)

  first_window = browser.window_handles[0]

  button = browser.find_element(By.TAG_NAME, "button")
  button.click()

  new_window = browser.window_handles[1]


  browser.switch_to.window(new_window)

  
  """
  browser.switch_to.window(first_window)
  """
  x = int(browser.find_element(By.ID, "input_value").text)
  y = calc(x)


  in1 = browser.find_element(By.ID, "answer")
  in1.send_keys(y)

  button = browser.find_element(By.TAG_NAME, "button")
  button.click()
  

  time.sleep(10)
  



finally:
  browser.quit()



