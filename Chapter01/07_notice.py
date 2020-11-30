import pyautogui

# 확인
a = pyautogui.alert(text='내용입니다', title='제목입니다', button='OK')
print(a)

# 여부
b = pyautogui.confirm(text='내용입니다', title='제목입니다', buttons=['OK', 'Cancel'])
print(b)

# 입력
c = pyautogui.prompt('What is your name?')
print(c)

# 비밀번호 입력, 문자열 표시하지 않음
d = pyautogui.password('Enter password (hidden mode)')
print(d)