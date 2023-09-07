
# Class representing a DisplayBoard in the system
class DisplayBoard:

    # Initialization of the DisplayBoard object
    def __init__(self, name):
        self.name = name  # Unique identifier for the display board
        self.data_to_display = []  # Data to be displayed on the board

    # Method to update the data on the display board
    def update_info(self, new_data):
        self.data_to_display.append(new_data)

    # Method to display the current data on the board
    def show(self):
        for data in self.data_to_display:
            print(data)
