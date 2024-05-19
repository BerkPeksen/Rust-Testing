import pyautogui
import time
import keyboard
import cv2


import pyautogui
import time
import keyboard

running = False  # Flag to control program execution

def start_stop():
    global running
    running = not running  # Toggle running state on each click

# Register hotkey to start/stop the automation (can be customized)
keyboard.add_hotkey('q', start_stop)

while True:
    if running:
        try:
            location = pyautogui.locateOnScreen('target.png', confidence=0.9)
            if location:
                x, y = pyautogui.center(location)
                pyautogui.click(x, y)
                print("Clicked on target!")
        except Exception as e:
            print("Target location not found:", e)
