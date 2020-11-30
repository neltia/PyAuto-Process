import pyautogui
import time
import webbrowser

webbrowser.open("http://www.gutenberg.org/")

time.sleep(2)
pyautogui.click(500, 500)
pyautogui.click(button='right')
pyautogui.press('t')