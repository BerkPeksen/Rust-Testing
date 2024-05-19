import pyautogui
import keyboard
import threading


clicking = False


num_threads = 10

def clicker():
    while clicking:
        pyautogui.click()

def toggle_clicking():
    global clicking
    if clicking:
        clicking = False
        print("Clicking stopped.")
    else:
        clicking = True
        print("Clicking started.")
        for _ in range(num_threads):
            threading.Thread(target=clicker).start()


keyboard.add_hotkey('s', toggle_clicking)

print("Press 'S' to start/stop clicking.")
print("Press 'esc' to exit.")


keyboard.wait('esc')