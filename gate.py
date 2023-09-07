
import paho.mqtt.client as mqtt
from utils.tauler import BusBoard

# Class representing a Gate (previously Stop) in the system
class Gate:

    # Initialization of the Gate object
    def __init__(self, gate_id, connection_parameters):
        self.gate_id = gate_id  # Unique identifier for the gate
        self.connection_parameters = connection_parameters  # MQTT connection parameters

        # Display board for the gate
        self.display_board = BusBoard(f"Display of Gate {gate_id}")
        self.client_propi = mqtt.Client(f"ClientOfGate_{gate_id}", userdata=self.display_board)

    # Method to activate the gate, making it listen for incoming messages and update its display board
    def activate(self):

        # Callback function to handle incoming MQTT messages
        def on_message_callback(client, userdata, message):
            decoded_message = message.payload.decode("utf-8")
            self.update_display(decoded_message)

        # Connect to MQTT server
        self.client_propi.connect(self.connection_parameters[2])  # localhost
        self.client_propi.subscribe(self.gate_id)
        self.client_propi.on_message = on_message_callback
        self.client_propi.loop_forever()

    # Method to update the gate's display board based on incoming messages
    def update_display(self, message):
        if message == "Final":
            print("End of communication.")
            self.client_propi.loop_stop()
        else:
            airplane_name, departure_time = message.split(",")
            # Update the display board with the airplane's name and departure time
            self.display_board.update_info((airplane_name, departure_time))
