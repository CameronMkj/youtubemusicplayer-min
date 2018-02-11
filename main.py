from pynput.keyboard import Key, Controller
import keyboard, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import mkj_pkg.main as mkj

if os.name == "nt":
    commandOne = 'cls'
else:
    commandOne = 'clear'
    os.system(commandOne)

browser = webdriver.Firefox()

keyboardTwo = Controller()
while True:
    if os.name == "nt":
        commandOne = 'cls'
    else:
        commandOne = 'clear'
    os.system(commandOne)

    if keyboard.is_pressed('ctrl'): ### Makes sure CTRL is pressed before issuing more commands.
        print("CTRL PRESSED")
        if keyboard.is_pressed('left'): ### GO BACK ONE SONG
            print("LEFT PRESSED")
            back = browser.find_element_by_css_selector(".ytp-prev-button")
            back.click()
        elif keyboard.is_pressed('right'):
            print('RIGHT PRESSED')
            next = browser.find_element_by_css_selector(".ytp-next-button")
            next.click()
        elif keyboard.is_pressed('up'):
            print('UP PRESSED')
        elif keyboard.is_pressed('down'):
            print('DOWN PRESSED')
        elif keyboard.is_pressed('end'):
            print("END PRESSED")
            pause = browser.find_element_by_css_selector(".ytp-play-button")
            pause.click()
        elif keyboard.is_pressed("del"):
            print("DEL PRESSED")
            mute = browser.find_element_by_css_selector(".ytp-mute-button")
            mute.click()
        # elif keyboard.is_pressed('home'):
        #     print("HOME PRESSED")
        #     skipper = browser.find_element_by_css_selector(".videoAdUiSkipButton")
        #     skipper.click()



        # if prss == True:
        #     pass


        # # PAUSE
        # elif wordS[0:5] == "start" or wordS[0:4] == "play":
        #     mkj.shortimportant("PAUSE WORKING")
        #     pause = browser.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
        #     pause.click()


        # elif wordS[0:4] == "skip":
        #     mkj.shortimportant("SKIP WORKING")
        #     skipper = browser.find_element_by_css_selector(".videoAdUiSkipButton")
        #     skipper.click()
        #                 # NEXT
        # elif wordS[0:4] == "stop" or wordS[0:5] == "pause":
        #     mkj.shortimportant("STOP WORKING")
        #     pause = browser.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
        #     pause.click()

        # # SEARCH
        # elif wordS[0:10] == "search for": 
        #     mkj.shortimportant("SEARCH WORKING")
        #     worder = str(wordS[11:50])
        #     youtubeMusic = str("https://www.youtube.com/results?search_query=" + worder)
        #     browser.get(youtubeMusic)