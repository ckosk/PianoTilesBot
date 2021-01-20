#RIP Flash... Script work on https://lagged.com/play/1501/

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:  810 Y:  770 RGB: ( 77,  80, 115)
#Tile 2 Position: X:  910 Y:  770 RGB: (  0,   0,   0)
#Tile 3 Position: X:  1010 Y:  770 RGB: ( 79,  82, 116)
#Tile 4 Position: X:  1110 Y:  770 RGB: ( 80,  83, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(810, 770)[0] == 0:
        click(810, 770)
    if pyautogui.pixel(910, 770)[0] == 0:
        click(910, 770)
    if pyautogui.pixel(1010, 770)[0] == 0:
        click(1010, 770)
    if pyautogui.pixel(1100, 770)[0] == 0:
        click(1110, 770)
