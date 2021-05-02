import webbrowser
import pyautogui
import time

url = 'https://overwatchleague.com/en-us/'

moveToX = 800
moveToY = 770
num_of_clicks = 2
secs_between_clicks = 1
#pyautogui.FAILSAFE= False
pyautogui.PAUSE = 2

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'
webbrowser.get(chrome_path).open(url)
time.sleep(3)
webbrowser.get(chrome_path).open(url)

#pyautogui.doubleClick(x=moveToX, y=moveToY, button='left')

pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

