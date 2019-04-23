import pyautogui
import random
screenWdith, screenHeight = pyautogui.size()
print(screenWdith)
print(screenHeight)




for x in range(0,27):
    alchSpell = pyautogui.locateOnScreen('images\HighAlchSpell.png')
    moveToSpellX, moveToSpellY = pyautogui.center(alchSpell)
    pyautogui.click(moveToSpellX, moveToSpellY, duration=1)

    magicShieldBow = pyautogui.locateOnScreen('images\MagicShieldbow.png')
    moveToShieldX, moveToShieldY = pyautogui.center(magicShieldBow)
    pyautogui.click(moveToShieldX, moveToShieldY, duration=1)



