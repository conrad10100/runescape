import pyautogui
screenWdith, screenHeight = pyautogui.size()
print(screenWdith)
print(screenHeight)


while pyautogui.FAILSAFE == True:
    for x in range(0, 27):
        alchSpell = pyautogui.locateOnScreen('images\HighAlchSpell.png', grayscale=True)
        moveToSpellX, moveToSpellY = pyautogui.center(alchSpell)
        pyautogui.click(moveToSpellX, moveToSpellY, duration=1)

        magicShieldBow = pyautogui.locateOnScreen('images\MagicShieldbow.png', grayscale=True)
        moveToShieldX, moveToShieldY = pyautogui.center(magicShieldBow)
        pyautogui.click(moveToShieldX, moveToShieldY, duration=1)