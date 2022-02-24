import csv
from hashtable import *
from shortest_path import *


delivery_one = []
delivery_two = []
delivery_three = []

truck_one_distance = []
truck_two_distance = []
truck_three_distance = []

package_to_street_address_dic_ = {}
street_address_to_location_id_dic = {}

# create hash table to store all packages' information
packages_hash_table = Hashtable()

# read package data from package.csv file
with open('package.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # store package information
    for row in csv_reader:
        package_id = int(row[0])
        delivery_status = 'At the hub'
        street_address = row[1]
        package_to_street_address_dic_[package_id] = street_address
        location_id = ''

        # read location data from locations.csv file
        with open('locations.csv') as csv_locations_:
            csv_reader_locations = csv.reader(csv_locations_, delimiter=',')
            # O(n)
            # find a location ID for every package
            for rows_ in csv_reader_locations:
                if rows_[2] == street_address:
                    location_id = rows_[0]

                    # store location street address and location ID in a dictionary
                    street_address_to_location_id_dic[street_address] = location_id

        # values = all package data to be stored in hash table
        values = [package_id, delivery_status, location_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7]]

        # distribute packages to three trucks depending on restrictions and requirements
        if '9:00:00' in row[5]:
            delivery_one.append(values)
        if '10:30:00' in row[5] and 'Delayed on flight---will not arrive to depot until 9:05 am' not in row[7]:
            delivery_one.append(values)
        if 'Can only be on truck 2' in row[7]:
            delivery_two.append(values)
        if 'Delayed on flight---will not arrive to depot until 9:05 am' in row[7] and '10:30:00' in row[5]:
            delivery_two.append(values)
        if 'Delayed on flight---will not arrive to depot until 9:05 am' in row[7] and 'EOD' in row[5]:
            delivery_three.append(values)
        if 'Wrong address listed' in row[7]:
            delivery_three.append(values)

        if values not in delivery_one and values not in delivery_two and values not in delivery_three:
            if len(delivery_three) < 14:
                delivery_three.append(values)
            else:
                delivery_two.append(values)

        # insert package into hash table
        packages_hash_table.insert(package_id, values)


# print data for all packages
def print_hashtable():
    packages_hash_table.print_hash()


# modify the delivery status for a package in the hash table
def update_delivery_status_(key, time_string):
    package = packages_hash_table.get_value_by_key(key)
    package[1] = time_string
    packages_hash_table.insert(key, package)


# delivery one - truck one
def get_path_truck_one():
    list_locations = []
    list_package_ids = []

    for x in delivery_one:
        list_locations.append(x[2])
        list_package_ids.append(x[0])

    clear_path()
    clear_distances()
    path_, distances_ = shortest_path(list_locations, '0')
    total_distance_truck_one = add_distances(distances_)
    truck_one_distance.append(total_distance_truck_one)
    # order packages (ids) by delivery route
    ordered_package_ids = []

    for locations in path_:
        for packages in list_package_ids:
            address = package_to_street_address_dic_[packages]
            if street_address_to_location_id_dic[address] == locations and packages not in ordered_package_ids:
                ordered_package_ids.append(packages)

    return path_, distances_, total_distance_truck_one, ordered_package_ids


def get_distance_truck_one():
    return truck_one_distance[0]


# delivery two - truck two
def get_path_truck_two():
    list_locations = []
    list_package_ids = []

    for x in delivery_two:
        list_locations.append(x[2])
        list_package_ids.append(x[0])

    clear_path()
    clear_distances()
    path_, distances_ = shortest_path(list_locations, '0')
    total_distance_truck_two = add_distances(distances_)
    truck_two_distance.append(total_distance_truck_two)
    # order packages (ids) by delivery route
    ordered_package_ids = []

    for locations in path_:
        for packages in list_package_ids:
            address = package_to_street_address_dic_[packages]
            if street_address_to_location_id_dic[address] == locations and packages not in ordered_package_ids:
                ordered_package_ids.append(packages)
    return path_, distances_, total_distance_truck_two, ordered_package_ids


def get_distance_truck_two():
    return truck_two_distance[0]


# delivery three - truck three
def get_path_truck_three():
    value = packages_hash_table.get_value_by_key(9)

    value[3] = '410 S State St.'
    value[6] = '84111'
    value[2] = '19'
    packages_hash_table.update(9, value)
    list_locations = []
    list_package_ids = []

    # O(1)
    for x in delivery_three:
        list_locations.append(x[2])
        list_package_ids.append(x[0])

    clear_path()
    clear_distances()
    path_, distances_ = shortest_path(list_locations, '0')
    total_distance_truck_three = add_distances(distances_)
    truck_three_distance.append(total_distance_truck_three)
    # order packages (ids) by delivery route
    ordered_package_ids = []

    # O(n^2)
    for locations in path_:
        for packages in list_package_ids:
            address = package_to_street_address_dic_[packages]
            if street_address_to_location_id_dic[address] == locations and packages not in ordered_package_ids:
                ordered_package_ids.append(packages)

    return path_, distances_, total_distance_truck_three, ordered_package_ids


def get_distance_truck_three():
    return truck_three_distance[0]


def distance_all():
    first = float(get_distance_truck_one())
    second = float(get_distance_truck_two())
    third = float(get_distance_truck_three())
    total = first + second + third
    return total
