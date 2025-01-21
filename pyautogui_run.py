import pyautogui as pg
import time

while True:
    try:
        pattern = pg.locateOnScreen('edu/next_page_tooltip.png')
        center = pg.center(pattern)
        pg.moveTo(center.x+47, center.y+62)
        pg.click()
        print('next pattern found and clicked')
    except:
        print('pattern not found')
    time.sleep(10)