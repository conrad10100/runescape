import pyautogui
import random
screenWdith, screenHeight = pyautogui.size()
print(screenWdith)
print(screenHeight)
##move mouse to high alch spell


while pyautogui.FAILSAFE == True:
    pyautogui.moveTo((screenWdith - screenWdith / 18)+random.randint(0, 6) , screenHeight - screenHeight / 7, duration=1)
    pyautogui.click()
    pyautogui.PAUSE = 2.5
    pyautogui.moveTo(screenWdith - screenWdith / 18, screenHeight - screenHeight / 5 , duration=1)
    pyautogui.click()

