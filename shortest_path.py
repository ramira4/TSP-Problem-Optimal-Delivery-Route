from distance import *
# path stores the location nodes in order
path = []
# distances stores the distances between path nodes
distances = []


#
# shortest_path is the method used to find the path traveled by each truck.
# The algorithm is an implementation of the 'Greedy' algorithm.
# It takes in a list of locations (every location that will be visited) and the current location
# (current location of iteration).
# The distance between every unvisited location and the current location is compared to find the shortest distance.
# The unvisited location with the shortest distance from the current location
# is selected as the next location to visit in the path.
# The unvisited location is appended to the path array and deleted from the list of unvisited locations.
# The distance to travel is appended to the distances array.
# The function is called again until all locations are visited.
#
#
def shortest_path(list_of_locations, current_location):

    current = current_location
    min_distance = 100
    for x in list_of_locations:
        distance = get_distance_between(int(current), int(x))
        if min_distance > distance:
            min_distance = distance
    for x in list_of_locations:
        distance = get_distance_between(int(current), int(x))
        if min_distance == distance:
            distances.append(min_distance)
            path.append(x)
            list_of_locations.pop(list_of_locations.index(x))
            shortest_path(list_of_locations, x)
    return path, distances


# clear path array
def clear_path():
    path.clear()


# clear distance array
def clear_distances():
    distances.clear()
