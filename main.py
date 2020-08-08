destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

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


def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attr_in_city in attractions_in_city:
        possible_attraction = attr_in_city
        attraction_tags = attr_in_city[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction)

    return attractions_with_interest


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

    # testing find_attractions
    la_arts = find_attractions("Los Angeles, USA", ["art"])
    print("\n")
    print(la_arts)
