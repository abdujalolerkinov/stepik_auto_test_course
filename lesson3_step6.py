import time
import math
from selenium import webdriver
link='http://suninjuly.github.io/redirect_accept.html'
try:
	browser=webdriver.Chrome()
	browser.get(link)
	btn=browser.find_element_by_class_name("trollface")	
	btn.click()
	time.sleep(1)
	new_window=browser.window_handles[1]
	browser.switch_to.window(new_window)
	num=int((browser.find_element_by_id("input_value")).text)
	y=str(math.log(abs(12*math.sin(num))))
	input=browser.find_element_by_id("answer")
	input.send_keys(y)
	btn1=browser.find_element_by_xpath("/html/body/form/div/div/button")
	btn1.click()
finally:
	time.sleep(10)
	browser.quit()