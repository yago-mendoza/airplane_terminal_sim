
# This file contains a timer class for the system

import time

# Class representing a Timer in the system
class Timer:

    # Initialization of the Timer object
    def __init__(self):
        self.start_time = None  # The time when the timer starts

    # Method to start the timer
    def start(self):
        self.start_time = time.time()

    # Method to get the elapsed time since the timer started
    def elapsed_time(self):
        if self.start_time is None:
            return 0
        return time.time() - self.start_time
