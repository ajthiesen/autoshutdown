python
import os
import time

# Set the time delay (in seconds)
delay = 3600

# Sleep for the delay period
time.sleep(delay)

# Shutdown the computer using the os.system() command
os.system("shutdown /s /t 1")
