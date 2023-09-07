
# This file seems to contain test or draft code based on its name "esborrany" which means "draft" in Catalan.

# Import necessary modules
import time
from utils.constants import minute
from utils.crono import Timer

# Sample code to test the timer's functionality
crono = Timer()
crono.start()
time.sleep(3 * minute)
print(f"Elapsed time: {crono.elapsed_time()} seconds")

# ... (Any additional test or draft code can be added here)
