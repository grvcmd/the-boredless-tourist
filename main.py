destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# function to identify each location based on its index in our destinations list.
def get_destination_index(destination):
    # variable to hold index of destination
    destination_index = destinations.index(destination)
    # index() method returns position at the first occurrence
    #   of the specified value.

    # returns destination_index as a string.
    return str(destination_index)


# function to get traveler's current location
def get_traveler_location(traveler):

    # The destination string of our example traveler is at index 1 of the list test_traveler.
    traveler_destination = traveler[1]

    # Retrieves index of the destination where the traveler is
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index


if __name__ == '__main__':
    # print(get_destination_index("Hyperabad, India"))

    test_destination_index = get_traveler_location(test_traveler)
    print(test_destination_index)
