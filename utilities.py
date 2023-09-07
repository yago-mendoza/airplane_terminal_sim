
# This file contains utility functions that are used throughout the system.

# Function to read data from a specified file and return the read data.
def readData(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

# ... (Any additional utility functions can be added here)
