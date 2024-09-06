#!pip install lackey

import lackey
import time

region = lackey.Region(590,300,100,90)
region_chapter = lackey.Region(500,360, 360, 180)
while True:
    try:
        region.click('safety_class_next_button.png')
        print('next pattern found and clicked')
    except:
        try:
            region_chapter.click('next_chapter.png')
            print('chapter pattern found and clicked')
        except:
            print('pattern not found')
    time.sleep(10)