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

    ##The values have to be off the line to cause the curve
    xOffCurve = ((xSpell+xItem)/2)+random.randint(-30, 30)
    yOffCurve = ((ySpell+yItem)/2)+random.randint(-30, 30)

    pyautogui.move(xSpell, ySpell, duration=1.5 + random.random())
    pyautogui.click(xSpell, ySpell)
    pyautogui.PAUSE = 0.3 + random.random()

    for t in range(0,3):
        xSpellToItem = (1-t/3)*(1-t/3)*xSpell+2*(1-t/3)*t/3*xOffCurve+t/3*t/3*xItem
        ySpellToItem = (1-t/3)*(1-t/3)*ySpell+2*(1-t/3)*t/3*yOffCurve+t/3*t/3*yItem
        pyautogui.move(xSpellToItem, ySpellToItem, duration=0.00, pause=None)


    pyautogui.move(xItem, yItem, duration=1)
    pyautogui.click(xItem, yItem)

#Added random values to avoid bot detection
while pyautogui.FAILSAFE == True:
    movement()