from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(750,380)[0] == 0:
        click(750,380)
    if pyautogui.pixel(880,380)[0] == 0:
        click(880,380)
    if pyautogui.pixel(1000,380)[0] == 0:
        click(1000,380)
    if pyautogui.pixel(1125,380)[0] == 0:
        click(1125,380)