import pyautogui
import random
screenWdith, screenHeight = pyautogui.size()
print(screenWdith)
print(screenHeight)
##move mouse to high alch spell


while pyautogui.FAILSAFE == True:
    xMagic = ((screenWdith - screenWdith / 18)+random.randint(100, 210))
    print(xMagic);
    pyautogui.moveTo((xMagic), (screenHeight - screenHeight / 7)-random.randint(30, 500), duration=0.1+random.random())
    pyautogui.click()
   ## pyautogui.PAUSE = 0.1 + random.random()
    pyautogui.moveTo((screenWdith - screenWdith / 18)+random.randint(120, 210), (screenHeight - screenHeight / 5)-random.randint(30, 405) , duration=0.1+random.random())
    pyautogui.click()

pyautogui.screenshot()
