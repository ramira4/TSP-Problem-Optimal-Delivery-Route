
from package import *
from schedule import *
import sys

print("-----------------------------------------------------------------------------------------------------------")
print("---------------------------------WELCOME TO THE WGUPS PROGRAM----------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------")


# prompt user choice action
def first_prompt():
    print("Please select an action:")
    print("1. Look up all packages by time")
    print("2. Look up total mileage traveled by all trucks at EOD")
    print("3. Quit program")
    print("-----------------------------------------------------------------------------------------------------------")
    selection = input("Type 1, 2, or 3 and press enter:")

    print("-----------------------------------------------------------------------------------------------------------")
# if user selects to view mileage, the distance traveled by each truck will be displayed and the total of all trucks
    if selection == '2':
        print("-----------------------------------------------------------------------------------------------------------")
        print("---------------------------------DISTANCES TRAVELED-----IN MILES-------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------")
        print("TOTAL DISTANCE TRAVELED BY TRUCK ONE: ")
        print(get_distance_truck_one())
        print("TOTAL DISTANCE TRAVELED BY TRUCK TWO: ")
        print(get_distance_truck_two())
        print("TOTAL DISTANCE TRAVELED BY TRUCK THREE: ")
        print(get_distance_truck_three())
        print("TOTAL DISTANCE TRAVELED BY ALL TRUCKS AT EOD: ")
        print(distance_all())
        print("-----------------------------------------------------------------------------------------------------------")
        first_prompt()

#  user selects to view package status at a specified time
    elif selection == '1':
        print("Please enter the time of day you would like to see all package statuses: ")
# take time in 24-hour format and then convert to time of day in float / fractional time
        time_input = input("Enter times in HH:MM 24-hour format (e.g. 14:05)\n").split()
        for time in time_input:
            hour, min = [int(i) for i in time.split(":")]
        minutes = min/60
        time_to_use = hour + minutes
# set packages to delivered up until the time specified by the user
        set_delivery_one_statuses(time_to_use)
        set_delivery_two_statuses(time_to_use)
        set_delivery_three_statuses(time_to_use)
        print("-----------------------------------------------------------------------------------------------------------")
        print("---------------------------------ALL PACKAGES--------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------")
# print all packages and their statuses at the specified time
        print_hashtable()

        print("-----------------------------------------------------------------------------------------------------------")
        first_prompt()
# allow user to exit program
    elif selection == '3':
        sys.exit()
    else:
        print("Invalid entry, please try again")
        first_prompt()


# initiate prompt
first_prompt()