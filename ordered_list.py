
# This file contains a class to manage ordered lists, which are used throughout the system for various purposes.

# Class representing an Ordered List
class OrderedList:

    # Initialization of the OrderedList object
    def __init__(self, elements=[]):
        # The elements are sorted to maintain the order
        self.elements = sorted(elements)

    # Method to add an element to the list
    # After adding, the list is sorted again to ensure order is maintained
    def add(self, element):
        self.elements.append(element)
        self.elements.sort()

    # Method to retrieve an element from the list by its index
    def get(self, index):
        return self.elements[index]

    # Method to get the position (index) of an element in the list
    def index(self, element):
        return self.elements.index(element)

    # Method to iterate through the list starting from a specific element
    # This is useful in contexts where we need to process elements from a certain point in the list
    def iterateFrom(self, element):
        index = self.index(element)
        while index < len(self.elements):
            yield self.elements[index]
            index += 1
