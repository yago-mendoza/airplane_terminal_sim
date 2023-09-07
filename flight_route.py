
from utils.lsts import LlistaOrdenada

# Class representing a FlightRoute (previously Line) in the system
class FlightRoute:

    # Initialization of the FlightRoute object
    def __init__(self, name, stops_and_times):
        self.name = name  # Unique identifier for the flight route
        self.stops_and_times = LlistaOrdenada(stops_and_times)  # Ordered list of stops and expected times

    # Method to calculate the expected time between two terminals (previously stops)
    def timeBetweenTerminals(self, start_terminal, end_terminal):
        start_time = self.stops_and_times[start_terminal]
        end_time = self.stops_and_times[end_terminal]
        return end_time - start_time
