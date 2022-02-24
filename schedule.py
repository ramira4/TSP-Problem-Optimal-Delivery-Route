from package import *
from shortest_path import *


# taking time as a float and turning it into time-HH:MM-string format
# O(1)
def string_format_time(time):
    hours = int(time)
    minutes = int((time * 60) % 60)
    if minutes < 10:
        return "%s:0%s" % (hours, minutes)
    else:
        return "%s:%s" % (hours, minutes)


# using time as a  float to get time traveled at 18mph given a distance

def get_time_traveled(distance):
    time = distance/18
    return time


# used to set package to en route when truck leaves hub

def set_delivery_en_route(key):
    update_delivery_status_(key, 'En Route')


# DELIVERY ONE
def set_delivery_one_statuses(time):
    # leave hub at 8:00 am with first set of packages in truck one
    truck_one_time = 8

    path, distances, total_distance, package_ids = get_path_truck_one()

    # start delivery and set packages to en route
    #
    if time >= 8:
        for x in package_ids:
            set_delivery_en_route(x)
    # complete deliveries only up until time input by user
    #
    while truck_one_time < time and len(distances) and len(package_ids):
        current_distance = distances[0]
        current_package = package_ids[0]
        time_passed = get_time_traveled(current_distance)
        truck_one_time = truck_one_time + time_passed
        time_to_set = string_format_time(truck_one_time)
        update_delivery_status_(current_package, ['Delivered at:', time_to_set])
        distances.pop(0)
        package_ids.pop(0)

# delivery 2
#
def set_delivery_two_statuses(time):
    # leave hub at 9:06 am with second set of packages in truck two
    truck_two_time = 9.1

    path, distances, total_distance, package_ids = get_path_truck_two()


    # start delivery and set packages to en route
    if time >= 9.1:
        for x in package_ids:
            set_delivery_en_route(x)
    # complete deliveries only up until time input by user

    while truck_two_time <= time and len(distances) and len(package_ids):
        current_distance = distances[0]
        current_package = package_ids[0]
        time_passed = get_time_traveled(current_distance)
        truck_two_time = truck_two_time + time_passed
        time_to_set = string_format_time(truck_two_time)
        update_delivery_status_(current_package, ['Delivered at:', time_to_set])
        distances.pop(0)
        package_ids.pop(0)


# delivery 3
def set_delivery_three_statuses(time):
    # leave hub at 11:00 am with third set of packages in truck three
    truck_three_time = 11

    path, distances, total_distance, package_ids = get_path_truck_three()

    # start delivery and set packages to en route
    if time >= 11:
        for x in package_ids:
            set_delivery_en_route(x)
    # complete deliveries only up until time input by user

    while truck_three_time <= time and len(distances) and len(package_ids):
        current_distance = distances[0]
        current_package = package_ids[0]
        time_passed = get_time_traveled(current_distance)
        truck_three_time = truck_three_time + time_passed
        time_to_set = string_format_time(truck_three_time)
        update_delivery_status_(current_package, ['Delivered at:', time_to_set])
        distances.pop(0)
        package_ids.pop(0)

