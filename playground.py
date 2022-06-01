import pyautogui
import time

print("This is a test")
print(pyautogui.size())
time.sleep(5)

print(pyautogui.position())
time.sleep(2)
pyautogui.click(100, 300)
pyautogui.typewrite("hello Geeks !")