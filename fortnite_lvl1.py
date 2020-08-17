import subprocess
import os
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


# Collect events until f10 was pressed
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
