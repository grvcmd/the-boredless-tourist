destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# attractions list will be an empty list for every destination in the destinations list.
attractions = [[] for attraction in destinations]


# function to identify each location based on its index in our destinations list.
def get_destination_index(destination):
    # variable to hold index of destination
    destination_index = destinations.index(destination)
        # index() method returns position at the first occurrence of the specified value.

    # returns destination_index as a string.
    return destination_index


# function to get traveler's current location
def get_traveler_location(traveler):
    # The destination string of our example traveler is at index 1 of the list test_traveler.
    traveler_destination = traveler[1]

    # Retrieves index of the destination where the traveler is
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index


def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
    except SyntaxError:
        return


if __name__ == '__main__':
    # print(get_destination_index("Hyperabad, India"))

    test_destination_index = get_traveler_location(test_traveler)
    print(test_destination_index)

    # Add attractions using the add_attraction variable
    add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
    add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
    add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
    add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
    add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
    add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
    add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
    add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
    add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
    add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
    add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

    print(attractions)
