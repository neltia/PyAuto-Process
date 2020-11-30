# selenium ver. 3.141.0
from selenium import webdriver

# Chrome
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.naver.com")
driver.quit() # 브라우저를 닫음

# Firefox
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.naver.com")
driver.quit()

# IE
driver = webdriver.Ie("IEDriverServer")
driver.get("https://www.naver.com")