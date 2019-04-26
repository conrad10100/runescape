import pyautogui

x0=3000
y0=500
x1=2700
y1=880
x2=2000
y2=300


def movement():


    pyautogui.moveTo(x0, y0, duration=1.0 )
    pyautogui.click()

    for t in range(0,10):
        xSpellToItem = (1-t/10)*(1-t/10)*x0+2*(1-t/10)*t/10*x1+t/10*t/10*x2
        ySpellToItem = (1-t/10)*(1-t/10)*y0+2*(1-t/10)*t/10*y1+t/10*t/10*y2
        pyautogui.mouseDown(xSpellToItem,ySpellToItem, duration=0.0, pause=None, tween=0)


    pyautogui.mouseDown()


while pyautogui.FAILSAFE == True:
    movement()