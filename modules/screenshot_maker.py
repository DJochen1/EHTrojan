import os
import pyautogui

def run(**args):
    print("[*] In de screenshot_maker module")
    image = pyautogui.screenshot()
    image.save("image.jpg")
    with open("image.jpg", "rb") as f:
        image_bytes = f.read()
    os.remove("image.jpg")
    return image_bytes