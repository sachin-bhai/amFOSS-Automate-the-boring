import pyautogui
import time

while True:
    pos=pyautogui.position()
    a=list(pos)
    pyautogui.moveTo(a[0]+1,a[1]+1,duration=0.25)
    time.sleep(10)

