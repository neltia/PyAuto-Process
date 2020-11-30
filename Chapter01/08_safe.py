import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 2

x, y = pyautogui.position()
print(x,y)

pyautogui.moveTo(500, 500)
pyautogui.moveTo(x,y)

pyautogui.moveTo(400, 400)
pyautogui.moveTo(x,y)