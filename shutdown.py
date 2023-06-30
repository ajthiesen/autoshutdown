#
#	shutdown.py
#	autoshutdown
#
#	Created by andrew@thiesen.co on 6/30/23.
#

#Import the necessary module.
python
import os
import time

# Set the time delay (in seconds) before the shutdown
delay = 3600

# Pause the execution of the program for the specified delay period using the time.sleep() function.
# This ensures that the program remains inactive for the specified delay period before proceeding to the next step.
time.sleep(delay)

### This line executes the system command to shut down the computer. The specific command used here is "shutdown /s /t 1". On Windows, the shutdown command is used, /s indicates a shutdown operation, and /t 1 sets a delay of 1 second before the shutdown. Depending on the operating system, you may need to modify this command. Please note that running this code will shut down the computer without further warning. Make sure to save any unsaved work before executing it. Also, use this code responsibly as unexpected system shutdowns can lead to data loss or other undesirable consequences.
os.system("shutdown /s /t 1")
