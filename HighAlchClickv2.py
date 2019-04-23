import pyautogui
import random
screenWdith, screenHeight = pyautogui.size()
print(screenWdith)
print(screenHeight)

alchSpell = pyautogui.locateCenterOnScreen('images\HighAlchSpell.png', )
moveToSpellX, moveToSpellY = pyautogui.center(alchSpell)
magicShieldBow = pyautogui.locateCenterOnScreen('images\MagicShieldbow.png')
moveToShieldX, moveToShieldY = pyautogui.center(magicShieldBow)

for i in range(0,10):


    pyautogui.moveTo(moveToSpellX, moveToSpellY, duration=1)
    pyautogui.click()






    pyautogui.moveTo(moveToShieldX, moveToShieldY, duration=1)
    pyautogui.click()


