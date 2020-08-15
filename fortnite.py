from pynput import keyboard
import subprocess
import psutil

# CONFIG - Replace with your data! #
PATH_TO_EXE = 'notepad.exe'
process_id = None


def on_press(key):
    # Necessary to access the process id
    global process_id

    # Open program when pressing f8
    if key == keyboard.Key.f8:
        process_id = subprocess.Popen(PATH_TO_EXE).pid
    # Close program when pressing f9 (do nothing if the program was not opened via f8)
    elif key == keyboard.Key.f9:
        if process_id:
            psutil.Process(process_id).terminate()
            process_id = None
    # Stop python program when pressing f10
    elif key == keyboard.Key.f10:
        # Stop listener
        return False


# Collect events until f10 was pressed
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
