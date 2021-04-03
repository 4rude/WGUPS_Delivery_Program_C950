import re  # Import the regular expression library
from PackageDelivery import *


def process_time(user_input):
    """
    process_time:
    process_time prints out a list of the packages and their respective status at a particular time, based on user
    input.

    Args:
    user_input: This string is taken in as user input that is in the form of military time

    Returns:
    n/a

    Raises:
    n/a

    Algorithmic complexity: O(n^2). The complexity is O(n^2) polynomial time because the deliver_packages method is
    O(n^2) and the for loop within the process_time method is O(n), so the O(n^2) complexity dominates the function
    complexity.
    """
    # Create a hash table with data on all the delivered packages
    all_package_statuses = deliver_packages()
    # Convert user_input from military time to a regular time object
    hour_string = user_input[0:2]
    minute_string = user_input[2:4]
    user_input_time = time(int(hour_string), int(minute_string))
    # Process user input to print out the data on each package and its status based on the given time compared to the
    # hub_time, transit_time, and delivery_time for each package in the hash table and display its
    for i in range(1, 41):
        # Create a package object with one of the package id's
        package = all_package_statuses.get(i)
        # Create a string that holds the status that will be returned for each package found
        status = ""
        # Add the package id to the status string
        status += "Package ID: " + package.package_id + ", "
        # Add the package address to the status string
        status += "Address: " + package.address + ", "
        # If the package hub time is less than the given time...
        if package.hub_time > user_input_time:
            status += "Hub Time: Not yet at hub, "
        else:  # If the package hub time is after the user inputted time...
            status += "Hub Time: " + str(package.hub_time) + ", "
        # If the package transit time is less than the given time...
        if package.transit_time > user_input_time:
            status += "Transit Time: Not yet in transit, "
        else:  # If the package transit time is after the user inputted time...
            status += "Transit Time: " + str(package.transit_time) + ", "
        # If the package delivery time is less than the given time...
        if package.delivery_time > user_input_time:
            status += "Delivery Time: Not yet delivered, "
            status += "Delivered by Truck: Not yet delivered "
        else:  # If the package delivery time is after the user inputted time...
            status += "Delivery Time: " + str(package.delivery_time) + ", "
            status += "Delivered by Truck: " + str(package.truck_id)
        # Print the status for the package
        print(status)
    print("Time processed.")


def validate_input(user_input):
    """
    validate_input:
    validate_input determines if user input matches a valid military time format.

    Args:
    user_input: This string is taken in as user input that is in the form of military time so it can be verified
    using a regular expression pattern.

    Returns:
    boolean: If the given user input matches the regex pattern True is returned, otherwise False is returned.

    Raises:
    n/a

    Algorithmic complexity: O(n). As far as my research tells me, searching a string for a regex pattern can vary
    from O(n) to a very complex function. My best estimate is O(n) because the regex module in Python is probably
    written well with complexity in mind. The n in O(n) is most likely the number of characters in a given string.
    """
    # Create regex pattern to match whether the given user_input is a valid military time
    regex = "^([01]\d|2[0-3])([0-5]\d)$"
    # Compare the user_input to the regex using the regex library search method
    result = re.search(regex, user_input)
    # If result matches, return true, if it does not return false
    if result is not None:
        return True
    else:
        return False

