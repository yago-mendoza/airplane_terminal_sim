
import paho.mqtt.client as mqtt
import time
import random

from utils.linia import Line
from utils.varies import llegirDades
from utils.constants import minut

# Class representing a Airplane in the system
class Airplane:

    # Initialization of the Airplane object
    def __init__(self, bus_id, line_belongs_to, n_torns, rest_time, connection_parameters):
        self.bus_id = bus_id  # Unique identifier for the bus
        self.n_torns = n_torns  # Number of rounds the bus will complete
        self.line_to_traverse = line_belongs_to  # Line the bus will traverse
        self.line_id = line_belongs_to.nom  # Line identifier
        self.rest_time = rest_time  # Time the bus will rest after completing a round
        self.connection_parameters = connection_parameters  # MQTT connection parameters

        # MQTT client for the bus
        self.client_propi = mqtt.Client(f"ClientDelAirplane_{bus_id}")

    # Method to activate the bus, making it traverse its line and publish its status
    def activate(self):

        # Connect to MQTT server
        self.client_propi.connect(self.connection_parameters[2])  # localhost

        # Loop through the specified number of rounds
        for torn_i in range(self.n_torns):
            print(f"{self.bus_id} ({self.line_id}) starts round {torn_i}")
            
            # Loop through each stop on the line
            for stop in iter(self.line_to_traverse):
                stop_actual, temps_fins_la_seguent = stop
                
                # Calculate time to next stop and publish
                for stop_restant, _ in self.line_to_traverse.iteraDesde(stop_actual):
                    temps_fins_arribada = self.line_to_traverse.timeBetweenStations(stop_actual, stop_restant)

                    info_per_enviar = f"{self.bus_id},{self.line_id},{temps_fins_arribada}"
                    self.client_propi.publish(stop_restant, info_per_enviar)

                # Calculate actual time to next stop (with some randomness)
                temps_fins_la_seguent_real = temps_fins_la_seguent + random.randint(0, int(0.5 * temps_fins_la_seguent))
                print(f"{self.bus_id} ({self.line_id}) leaves {stop_actual}. Expected time {temps_fins_la_seguent} m, but actual time {temps_fins_la_seguent_real} m\n")
                
                # Sleep for the time it takes to reach the next stop
                time.sleep(temps_fins_la_seguent_real*minut)
            
            print(f"{self.bus_id} ({self.line_id}) ends round {torn_i}")
            
            # Resting time for the bus
            time.sleep(self.rest_time*minut)

# Function to create and activate a bus based on provided parameters
def bus(bus_id, line_id, n_torns, rest_time, connection_parameters):

    # Read data from data file
    data_linies, _, _, _ = llegirDades("data.txt")
    line_belongs_to = Line(line_id, data_linies[line_id])

    # Create and activate the bus
    bus_creat = Airplane(bus_id, line_belongs_to, n_torns, rest_time, connection_parameters)
    bus_creat.activate()
