import pyautogui
screenWdith, screenHeight = pyautogui.size()
print(screenWdith)
print(screenHeight)

alchSpell = pyautogui.locateOnScreen('images\HighAlchSpell.png', grayscale=True)
moveToSpellX, moveToSpellY = pyautogui.center(alchSpell)

magicShieldBow = pyautogui.locateOnScreen('images\MagicShieldbow.png', grayscale=True)
moveToShieldX, moveToShieldY = pyautogui.center(magicShieldBow)
while pyautogui.FAILSAFE == True:
    for x in range(0, 27):

        pyautogui.click(moveToSpellX, moveToSpellY, duration=2)
        pyautogui.PAUSE=4

        pyautogui.click(moveToShieldX, moveToShieldY, duration=2)
        pyautogui.PAUSE = 4