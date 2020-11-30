import pyautogui
import time

width, height = pyautogui.size()
print('width={0}, height={1}'.format(width, height))  
x, y = pyautogui.position()
print(x,y)

pyautogui.moveTo(500, 500)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(x,y)