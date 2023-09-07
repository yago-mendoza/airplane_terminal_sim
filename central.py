
# This file contains the main logic to manage the system's operations

import time
from utils.constants import minute
from utils.bus import Airplane
from utils.parada import Gate

# Constants for connection parameters
BROKER = "localhost"
PORT = 1883
CONNECTION_PARAMETERS = ("", "", BROKER, PORT)

# Create and activate airplanes
airplane1 = Airplane("A1", "L1", 3, 10, CONNECTION_PARAMETERS)
airplane1.activate()
airplane2 = Airplane("A2", "L1", 3, 10, CONNECTION_PARAMETERS)
airplane2.activate()

# Create and activate gates
gate1 = Gate("G1", CONNECTION_PARAMETERS)
gate1.activate()
gate2 = Gate("G2", CONNECTION_PARAMETERS)
gate2.activate()

# ... (Additional logic to manage the system's operations can be added here)
