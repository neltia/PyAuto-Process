# selenium ver. 3.141.0
from selenium import webdriver

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.google.com")

input_box = driver.find_element_by_name("q")
input_box.send_keys("python")
input_box.submit()