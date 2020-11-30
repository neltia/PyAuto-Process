import pyautogui
import time

filename = 'six.png'

pyautogui.hotkey("win","r")
pyautogui.write("calc.exe")
pyautogui.press("enter")
time.sleep(3)

# 이미지 위치
six_btn = pyautogui.locateOnScreen(filename)
print(six_btn)

# 중앙 좌표
center = pyautogui.center(six_btn) # locateCenterOnScreen(six_btn)
pyautogui.click(center)