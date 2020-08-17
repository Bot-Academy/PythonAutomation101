import subprocess
import os
import pyautogui
import time
from pynput import keyboard

# CONFIG - Replace if you want to use another application! #
PATH_TO_EXE = 'C:/Program Files/Epic Games/Fortnite/FortniteGame/Binaries/Win64/FortniteLauncher.exe'
FORTNITE_PROCESS_NAME = 'FortniteClient-Win64-Shipping'


def on_press(key):
    # Open program when pressing f8
    if key == keyboard.Key.f8:
        subprocess.run(PATH_TO_EXE)
    # Close program when pressing f9
    elif key == keyboard.Key.f9:
        os.system(f'taskkill /f /im {FORTNITE_PROCESS_NAME}.exe')
    # Stop python program when pressing f10
    elif key == keyboard.Key.f10:
        # Stop listener
        return False


# Collect events until f10 was pressed (started as background process)
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Run forever (program can be terminated with the listener [f10])
while True:
    screenshot = pyautogui.screenshot()
    if screenshot.getpixel((1720, 334)) > (250, 250, 250) or screenshot.getpixel((1695, 334)) > (250, 250, 250):
        # In game, do nothing
        print('In game')
    elif screenshot.getpixel((1605, 605)) == (82, 93, 101):
        # Waiting in queue, do nothing
        print('In waiting queue')
    elif screenshot.getpixel((1500, 680)) == (0, 108, 255):
        # Died (or won) -> Click Ready Up
        pyautogui.click(1500, 680)
        print('Clicked on Ready Up')
    elif screenshot.getpixel((1863, 1015)) == (255, 255, 255):
        # Start Screen -> Click Battle Royale
        pyautogui.click(950, 350)
        print('Clicked on Battle Royale')
    elif screenshot.getpixel((1550, 600)) == (246, 255, 0):
        # Lobby with visible Play button -> Click Play button
        pyautogui.click(1550, 600)
        print('Clicked on Play button')
    elif screenshot.getpixel((900, 1050)) == (0, 0, 116):
        # Lobby with no visible Play button -> Activate Play tab
        pyautogui.click(550, 50)
        print('Clicked on Play tab')
    else:
        print('Unknown state')
    time.sleep(5)
