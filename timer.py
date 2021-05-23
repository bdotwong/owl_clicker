# import the time module
import time
import pyautogui
import webbrowser
x = 850
y = 380


url = "https://overwatchleague.com/en-us"

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print("Opening OW")
    open_ow()
  
  
# input time in seconds
t = input("Enter the time in seconds: ")



def open_ow():
    # MacOS
    #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.get(chrome_path).open(url)
    #webbrowser.open_new(url)
    time.sleep(2)
    pyautogui.doubleClick(x, y)  # Move the mouse to XY coordinates and click it.

    
# function call
countdown(int(t))