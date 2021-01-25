from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32api, win32con

#color = 255,219,195

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(575,445,750,525))
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))

            if b == 195:
                click(x+575,y+445)
                time.sleep(0.05)
                break