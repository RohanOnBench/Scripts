import pyautogui as screen
import random
import time

screen.FAILSAFE=False
x,y=screen.size()
while True:
    # x1=random.randint(0,x)
    # y1=random.randint(0,y)
    # screen.moveTo(x1,y1)
    time.sleep(10)
    screen.press('space')
    screen.hotkey('shift','3')

    
