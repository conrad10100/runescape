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


def movement():
    xSpell = magicSpellX + random.randint(-3, 18)
    ySpell = magicSpellY + random.randint(-15, 5)

    xItem = itemX + random.randint(-3, 20)
    yItem = itemY + random.randint(-20, 0)

    xOffCurve = (xSpell+xItem)/2
    yOffCurve = (ySpell+yItem)/2

    pyautogui.mouseDown(xSpell, ySpell, duration=1.0 + random.random())
    pyautogui.click()
    pyautogui.PAUSE = .3 + random.random()
    for t in range(0,1):
        xSpellToItem = xOffCurve + (1 - t) * (1 - t) * (xSpell - xOffCurve) + t * t * (xItem - xOffCurve)
        ySpellToItem = yOffCurve + (1 - t) * (1 - t) * (ySpell - yOffCurve) + t * t * (yItem - yOffCurve)
        pyautogui.moveTo(xSpellToItem,ySpellToItem, duration=0, pause=None)


    pyautogui.moveTo(xItem, yItem, duration=1.0 + random.random())
    pyautogui.click()
    pyautogui.PAUSE = .3 + random.random()


#Added random values to avoid bot detection
while pyautogui.FAILSAFE == True:
    movement()