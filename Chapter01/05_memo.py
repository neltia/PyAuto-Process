import pyautogui
import clipboard
import time

memo = """\
오늘의 메모.
PyAutoGui라는 파이썬 언어를 사용한 자동화 모듈을 학습했다.
모듈을 사용해 어렵지 않게 매크로 프로그램을 만들 수 있다.
"""
clipboard.copy(memo)

pyautogui.hotkey("win","r")
pyautogui.write("notepad.exe")
pyautogui.press("enter")
time.sleep(1)

pyautogui.hotkey("ctrl","v")
time.sleep(1)

pyautogui.hotkey("ctrl","s")
pyautogui.write("test.txt")
pyautogui.hotkey("alt","S")