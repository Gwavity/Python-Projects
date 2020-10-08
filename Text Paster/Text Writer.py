import time
import pyautogui


with open('something.txt') as some:
    some = some.readlines()
    time.sleep(3)

    for txt in some:
        time.sleep(.5)
        pyautogui.write(txt.strip())
        pyautogui.press('enter')

