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


if __name__ == '__main__':
    print(get_destination_index("Los Angeles, USA"))