import pyautogui
import time

def find_color(hex_color):
    # Loop to continuously check for the specified color
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        # Get the color at the current mouse position
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        print(pixel_color)
        # Check if the color matches the specified color
        if pixel_color == hex_color:
            # Perform a left click
            pyautogui.click()
            # Pause for a short time to avoid multiple clicks
            print("Color Found")
            time.sleep(0.1)
        else:
            print("Colot not found")    

# Specify the color in hexadecimal format (e.g., white: 0xFFFFFF)
color_to_find = (75, 219, 106)  # Black color, replace with your desired color


find_color(color_to_find)