import pyautogui

pyautogui.FAILSAFE = False

while True:
    x, y = pyautogui.position()
    screenX, screenY = pyautogui.size()
    isGone = False
    # X teleport
    if x == 0 and not isGone:
        pyautogui.moveTo(screenX-1, y)
        isGone == True
    if x == screenX-1 and not isGone:
        pyautogui.moveTo(0, y)
        isGone == True
    if x > 0 and x < screenX-1:
        isGone = False
    # Y teleport
    if y == 0 and not isGone:
        pyautogui.moveTo(x, screenY-1)
        isGone == True
    if y == screenY-1 and not isGone:
        pyautogui.moveTo(x, 0)
        isGone == True
    if y > 0 and y < screenY-1:
        isGone = False