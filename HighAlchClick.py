import pyautogui
import random

screenWdith, screenHeight = pyautogui.size()
magicSpellX = screenWdith - screenWdith / 18
magicSpellY = screenHeight - screenHeight / 7
itemX = (screenWdith - screenWdith / 18)
itemY = (screenHeight - screenHeight / 5)
print(magicSpellX)
print(magicSpellY)
print(screenWdith)
print(screenHeight)
print(itemY)

#Added random values to avoid bot detection
while pyautogui.FAILSAFE == True:
    xSpell = magicSpellX + random.randint(-3, 18)
    ySpell = magicSpellY + random.randint(-15, 5)
    pyautogui.moveTo(xSpell, ySpell, duration=1.0 + random.random())
    pyautogui.click()
    pyautogui.PAUSE = .3 + random.random()
    xItem = itemX + random.randint(-3, 20)
    yItem = itemY + random.randint(-20, 0)
    pyautogui.moveTo(xItem, yItem, duration=1.0 + random.random())
    pyautogui.click()
    pyautogui.PAUSE = .3 + random.random()
