import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link="http://suninjuly.github.io/explicit_wait2.html"
try:
	browser=webdriver.Chrome()
	#browser.implicitly_wait(5)
	browser.get(link)
	WebDriverWait(browser, 20).until(
			EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100') )
	btn1=browser.find_element_by_id("book")
	btn1.click()
	time.sleep(2)
	x=int(browser.find_element_by_id("input_value").text)
	y=str(math.log(abs(12*math.sin(x))))
	input=browser.find_element_by_id("answer")
	input.send_keys(y)
	btn2=browser.find_element_by_id("solve")
	btn2.click()
finally:
	time.sleep(10)
	browser.quit()