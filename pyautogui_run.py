import pyautogui as pg
import time

dx = 47
dy = 62

count = 0
while True:
    try:
        # pattern = pg.locateOnScreen('edu/next_page_tooltip.png', confidence=0.95)
        # center = pg.center(pattern)
        center = pg.locateCenterOnScreen('edu/next_page_tooltip2.png', confidence=0.95, region = (1120, 660, 1260, 790))
        pg.moveTo(center.x+dx, center.y+dy)
        pg.click()
        print('!')
    except:
        count += 1
        if count<6:
            print('.',end='')
        else:
            print('.')
            count = 0
    time.sleep(10)


count = 0
while True:
    try:
        # pattern = pg.locateOnScreen('edu/next_page_tooltip.png', confidence=0.95)
        # center = pg.center(pattern)
        center = pg.locateCenterOnScreen('edu/next_page_tooltip.png', confidence=0.95)
        pg.moveTo(center.x+dx, center.y+dy)
        pg.click()
        print('1')
    except:
        try:
            pattern = pg.locateOnScreen('edu/next_page_tooltip2.png', confidence=0.95)
            center = pg.center(pattern)
            pg.moveTo(center.x+47, center.y+62)
            pg.click()
            print('2')
        except:
            try:
                pattern = pg.locateOnScreen('edu/next_page_tooltip3.png', confidence=0.95)
                center = pg.center(pattern)
                pg.moveTo(center.x+47, center.y+62)
                pg.click()
                print('3')
            except:        
                count += 1
                if count<6:
                    print('.',end='')
                else:
                    print('.')
                    count = 0
    time.sleep(10)