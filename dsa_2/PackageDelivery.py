from PackageCSVReader import *
from DistanceCSVReader import *
from Truck import *
from datetime import *


def deliver_packages():
    """
    deliver_packages:
    The deliver_packages function is the main algorithm to initialize the distance dictionary and package hash table,
    initialize and update truck data, load packages into the truck, initialize and update the package_hash_table hash
    table (which stores the packages), organize which packages must be delivered in which order, deliver the packages,
    and finally return the hash table of package information so a user can access the data after the program has been
    ran.

    Args:
    n/a

    Returns:
    package_hash_table: The package_hash_table object is a Hash Table object instance that holds all of the package
    information from the package csv file, as well as other parameters that hold delivery information. It is used to
    add and update data relating to each package that must be delivered. The hash table is key to showing package
    and delivery information to users of the command line interface.

    Raises:
    n/a

    Algorithmic complexity: O(n). If this hash table had to resize or had more than one element per key, then it could
    be O(n^2), but since we know it does not, then it us O(n). This is due to each element in the truck_list list being
    iterated over.
    """
    # Initialize a hash table with all the packages
    package_hash_table = package_reader()
    # Initialize a dictionary with all of the delivery locations and distances
    distance_dict = distance_reader()
    # -------------------------------- Manually loading packages -------------------------------- #
    # No more than 16 packages per truck
    # Truck one holds all packages that must be delivered before 9-10:30am and are NOT delayed
    truck_one_list = [13, 14, 15, 16, 34, 19, 20, 21, 4, 40]
    # Truck two holds all the not-delayed packages that must be delivered on truck 2 required packages
    truck_two_list = [3, 18, 12, 36, 37, 38]
    # List of delayed packages that are on the second truck
    delayed_packages = [6, 25, 28, 32]
    # This list holds the rest of the pre-10:30am packages besides the ones that must be delivered on truck 2
    truck_three_list = [6, 25, 26, 1, 28, 7, 29, 30, 31, 32]
    # Create string to hold hub address
    hub_address = "4001 South 700 East"

    # Add package data and initialize package time info into the Package Hash Table
    update_hub_time(package_hash_table, truck_one_list, time(8, 0))
    update_hub_time(package_hash_table, truck_two_list, time(8, 0))
    update_hub_time(package_hash_table, truck_three_list, time(8, 0))
    update_hub_time(package_hash_table, delayed_packages, time(9, 5))

    # -------------------------------- TRUCK ONE DELIVERY CODE -------------------------------- #
    # TRUCK ONE GOES OUT AT THE SAME TIME AS TRUCK TWO (BOTH FIRST)
    # Run the algorithm to organize the truck package list so it can be delivered in the most efficient way
    truck_one_list = delivery_algorithm(truck_one_list)

    # Create truck objects to hold packages. Initialize time to current time. Load organized packages.
    truck_one = Truck(1, time(8, 0), truck_one_list)

    # Set the truck's current location to the WGUPS hub
    truck_one.current_location = hub_address

    # Print lines for formatting
    print("----------------------------------")
    # Print out a header for the truck deliveries
    print("Truck Delivery Schedule: ")
    # Print lines for formatting
    print("----------------------------------")
    # Print out when truck one leaves
    print("Truck one leaves at", truck_one.time)

    # Update the transit time to 8am, as this is the first set of packages that need to be delivered
    update_transit_time(package_hash_table, truck_one_list, time(8, 0))

    # Deliver truck one packages until there are no packages left (while truck is not empty...)
    while truck_one.package_list:
        # Create the package object that holds data on the first/next package that needs to be delivered
        package = package_hash_table.get(truck_one.package_list[0])
        # Get the distance to the next address
        distance_to_next_address = distance_dict[truck_one.current_location][package.address]
        # Add the amount of miles that is needed to deliver the next package
        truck_one.miles += float(distance_to_next_address)
        # Add the package address to the trucks new address
        truck_one.current_location = package.address
        # Update the current truck time to the time that it took to drive to the next destination
        truck_one.time = add_time(miles_to_time(distance_to_next_address), truck_one.time)
        # Update the package delivery time to the current truck time (when the truck arrived at the destination)
        package.delivery_time = truck_one.time
        # Add the id of the truck to the package so we know which truck delivered which package
        package.truck_id = truck_one.truck_id
        # Update the package information in the package hash table
        package_hash_table.set(int(package.package_id), package)
        # Remove the first package in the objects truck list
        truck_one.package_list.pop(0)
        # If truck is empty, use current address to determine distance from current address to hub, add that amount on
        # to the truck miles, and that amount of time on to the truck time
        if not truck_one.package_list:
            truck_one.miles += float(distance_dict[truck_one.current_location][hub_address])
            # Update the truck's current location to the hub address
            truck_one.current_location = hub_address

    # Set truck one return time to current time (truck has returned to the hub)
    truck_one.return_time = truck_one.time

    # Print truck return time
    print("Truck one return time:", truck_one.return_time)

    # -------------------------------- TRUCK TWO DELIVERY CODE -------------------------------- #
    # TRUCK TWO GOES OUT AT THE SAME TIME AS TRUCK ONE
    # Run the algorithm to organize the truck package list so it can be delivered in the most efficient way
    truck_two_list = delivery_algorithm(truck_two_list)

    # Create truck two to hold next list of packages. Set current truck time to previous trucks return time.
    # Load organized packages.
    truck_two = Truck(2, time(8, 0), truck_two_list)

    # Set the truck's current location to the WGUPS hub
    truck_two.current_location = hub_address

    # Print out when truck two leaves
    print("Truck two leaves at", truck_two.time)

    # Update the transit time of all packages in the truck two list with the return time of truck one (truck two
    # leaves when truck one returns).
    update_transit_time(package_hash_table, truck_two_list, time(8, 0))

    # Deliver truck two packages until there are no packages left (while truck is not empty...)
    while truck_two.package_list:
        # Create the package object that holds data on the first/next package that needs to be delivered
        package = package_hash_table.get(truck_two.package_list[0])
        # Get the distance to the next address
        distance_to_next_address = distance_dict[truck_two.current_location][package.address]
        # Add the amount of miles that is needed to deliver the next package
        truck_two.miles += float(distance_to_next_address)
        # Add the package address to the trucks new address
        truck_two.current_location = package.address
        # Update the current truck time to the time that it took to drive to the next destination
        truck_two.time = add_time(miles_to_time(distance_to_next_address), truck_two.time)
        # Update the package delivery time to the current truck time (when the truck arrived at the destination)
        package.delivery_time = truck_two.time
        # Add the id of the truck to the package so we know which truck delivered which package
        package.truck_id = truck_two.truck_id
        # Update the package information in the package hash table
        package_hash_table.set(int(package.package_id), package)
        # Remove the package that is in the front of the list and was just delivered
        truck_two.package_list.pop(0)
        # If truck is empty, use current address to determine distance from current address to hub, add that amount on
        # to the truck miles, and that amount of time on to the truck time
        if not truck_two.package_list:
            truck_two.miles += float(distance_dict[truck_two.current_location][hub_address])
            # Update the truck's current location to the hub address
            truck_two.current_location = hub_address

    # Set truck two return time to current time (meaning the truck has returned to the hub)
    truck_two.return_time = truck_two.time
    # Print truck return time
    print("Truck two return time:", truck_two.return_time)

    # -------------------------------- TRUCK THREE DELIVERY CODE -------------------------------- #
    # TRUCK THREE GOES OUT AFTER TRUCK ONE RETURNS
    # Run the algorithm to organize the truck package list so it can be delivered in the most efficient way
    truck_three_list = delivery_algorithm(truck_three_list)

    # Create truck three to hold next list of packages. Set current truck time to previous trucks return time.
    truck_three = Truck(3, truck_one.return_time, truck_three_list)

    # Set the truck's current location to the WGUPS hub
    truck_three.current_location = hub_address

    # Print out when truck three leaves
    print("Truck three leaves at", truck_three.time)

    # Update the transit time of all packages in the truck three list with the return time of truck one (truck three
    # leaves when truck two returns).
    update_transit_time(package_hash_table, truck_three_list, time(9, 5))

    # Deliver truck three packages until there are no packages left (while truck is not empty...)
    while truck_three.package_list:
        # Create the package object that holds data on the first/next package that needs to be delivered
        package = package_hash_table.get(truck_three.package_list[0])
        # Get the distance to the next address
        distance_to_next_address = distance_dict[truck_three.current_location][package.address]
        # Add the amount of miles that is needed to deliver the next package
        truck_three.miles += float(distance_to_next_address)
        # Add the package address to the trucks new address
        truck_three.current_location = package.address
        # Update the current truck time to the time that it took to drive to the next destination
        truck_three.time = add_time(miles_to_time(distance_to_next_address), truck_three.time)
        # Update the package delivery time to the current truck time (when the truck arrived at the destination)
        package.delivery_time = truck_three.time
        # Add the id of the truck to the package so we know which truck delivered which package
        package.truck_id = truck_three.truck_id
        # Update the package information in the package hash table
        package_hash_table.set(int(package.package_id), package)
        # Remove the first package in the objects truck list
        truck_three.package_list.pop(0)
        # If truck is empty, use current address to determine distance from current address to hub, add that amount on
        # to the truck miles, and that amount of time on to the truck time
        if not truck_three.package_list:
            truck_three.miles += float(distance_dict[truck_three.current_location][hub_address])
            # Update the truck's current location to the hub address
            truck_three.current_location = hub_address

    # Set truck three return time to current time (meaning the truck has returned to the hub)
    truck_three.return_time = truck_three.time
    # Print truck return time & mileage
    print("Truck three return time:", truck_three.return_time)

    # -------------------------------- TRUCK ONE SECOND DELIVERY CODE -------------------------------- #
    # TRUCK ONE GOES OUT AGAIN AFTER TRUCK TWO RETURNS
    # Re-fill truck_one_list with the rest of the packages
    truck_one_list = [11, 22, 23, 24]

    # Run the algorithm to organize the truck package list so it can be delivered in the most efficient way
    truck_one_list = delivery_algorithm(truck_one_list)

    # Add the truck one list to the package list variable of truck one
    truck_one.package_list = truck_one_list

    # Re-set the truck one's current location to the hub address
    truck_one.current_location = hub_address

    # Re-set the current time of truck one so it reflects when truck two returns (so truck one can leave)
    truck_one.time = truck_two.return_time

    # Print out when truck one leaves again to deliver packages
    print("Truck one leaves again at", truck_one.time)

    # Update the hub time for all of the packages in the newly loaded truck one
    update_hub_time(package_hash_table, truck_one_list, time(8, 0))

    # Update the transit time of all packages in the truck one list with the return time of truck two (truck one
    # leaves when truck three returns).
    update_transit_time(package_hash_table, truck_one_list, truck_two.return_time)

    # Deliver packages while the trucks package list is not empty
    while truck_one.package_list:
        # Create the package object that holds data on the first/next package that needs to be delivered
        package = package_hash_table.get(truck_one.package_list[0])
        # Get the distance to the next address
        distance_to_next_address = distance_dict[truck_one.current_location][package.address]
        # Add the amount of miles that is needed to deliver the next package
        truck_one.miles += float(distance_to_next_address)
        # Add the package address to the trucks new address
        truck_one.current_location = package.address
        # Update the current truck time to the time that it took to drive to the next destination
        truck_one.time = add_time(miles_to_time(distance_to_next_address), truck_one.time)
        # Update the package delivery time to the current truck time (when the truck arrived at the destination)
        package.delivery_time = truck_one.time
        # Add the id of the truck to the package so we know which truck delivered which package
        package.truck_id = truck_one.truck_id
        # Update the package information in the package hash table
        package_hash_table.set(int(package.package_id), package)
        # Remove the first package in the objects truck list
        truck_one.package_list.pop(0)
        # If truck is empty, use current address to determine distance from current address to hub, add that amount on
        # to the truck miles, and that amount of time on to the truck time
        if not truck_one.package_list:
            truck_one.miles += float(distance_dict[truck_one.current_location][hub_address])
            # Update the truck's current location to the hub address
            truck_one.current_location = hub_address

    # Set truck one return time to current time (meaning the truck has returned to the hub)
    truck_one.return_time = truck_one.time
    # Print truck return time
    print("Truck one re-return time:", truck_one.return_time)

    # -------------------------------- TRUCK TWO SECOND DELIVERY DELIVERY CODE -------------------------------- #
    # TRUCK TWO GOES OUT AT THE SAME TIME AS TRUCK ONE
    # Load up the truck two list with the rest of the packages
    truck_two_list = [5, 8, 9, 10, 17, 2, 33, 39, 27, 35]
    # Run the algorithm to organize the truck package list so it can be delivered in the most efficient way
    truck_two_list = delivery_algorithm(truck_two_list)

    # Update truck two to hold next list of packages.
    # Load organized packages.
    truck_two.package_list = truck_two_list

    # Set the truck's current location to the WGUPS hub
    truck_two.current_location = hub_address

    # Truck two leaves when package #9 gets the updated address
    truck_two.time = truck_three.return_time

    # Print out when truck two leaves again to deliver packages
    print("Truck two leaves again at", truck_two.time)

    # Update the hub time for all of the packages in the newly loaded truck one
    update_hub_time(package_hash_table, truck_two_list, time(8, 0))
    # Update the transit time of all packages in the truck two list with the return time of truck three (truck two
    # leaves when truck one returns).
    update_transit_time(package_hash_table, truck_two_list, truck_three.return_time)

    # Deliver truck two packages until there are no packages left (while truck is not empty...)
    while truck_two.package_list:
        # Create the package object that holds data on the first/next package that needs to be delivered
        package = package_hash_table.get(truck_two.package_list[0])
        # Get the distance to the next address
        distance_to_next_address = distance_dict[truck_two.current_location][package.address]
        # Add the amount of miles that is needed to deliver the next package
        truck_two.miles += float(distance_to_next_address)
        # Add the package address to the trucks new address
        truck_two.current_location = package.address
        # Update the current truck time to the time that it took to drive to the next destination
        truck_two.time = add_time(miles_to_time(distance_to_next_address), truck_two.time)
        # Update the package delivery time to the current truck time (when the truck arrived at the destination)
        package.delivery_time = truck_two.time
        # Add the id of the truck to the package so we know which truck delivered which package
        package.truck_id = truck_two.truck_id
        # Update the package information in the package hash table
        package_hash_table.set(int(package.package_id), package)
        # Remove the package that is in the front of the list and was just delivered
        truck_two.package_list.pop(0)
        # If truck is empty, use current address to determine distance from current address to hub, add that amount on
        # to the truck miles, and that amount of time on to the truck time
        if not truck_two.package_list:
            truck_two.miles += float(distance_dict[truck_two.current_location][hub_address])
            # Update the truck's current location to the hub address
            truck_two.current_location = hub_address

    # Set truck two return time to current time (meaning the truck has returned to the hub)
    truck_two.return_time = truck_two.time
    # Print truck return time
    print("Truck two re-return time:", truck_two.return_time)

    # -------------------------------- END-OF-DAY DELIVERY INFO CODE -------------------------------- #

    # Determine the delivery mileage of all the trucks combined
    all_truck_mileage = truck_one.miles + truck_two.miles + truck_three.miles
    print("----------------------------------")
    print("Total mileage for deliveries:", round(all_truck_mileage, 2))
    print("-------------------")
    print("Packages Delivered.")
    print("-------------------")

    # Finally return the package_statuses Hash Table holding package status data for the user to view
    return package_hash_table


def update_hub_time(hash_table, truck_list, hub_time):
    """
    update_hub_time:
    The update_hub_time method takes in a hash table, list, and time as arguments. For each package id in the list
    of packages to be delivered, get the specified package out of the hash table, update its hub time with the given
    hub_time, and set the hash table key to a new value.

    Args:
    hash_table: The hash table is an object reference passed in so the contents can be updated with new hub time data.
    truck_list: The truck list is a list of package id's that should have their hub time updated.
    hub_time: The hub time parameter is a time object that updates the current hub time for a package object.

    Returns:
    n/a

    Raises:
    n/a

    Algorithmic complexity: O(n). If this hash table had to resize or had more than one element per key, then it could
    be O(n^2), but since we know it does not, then it us O(n). This is due to each element in the truck_list list being
    iterated over.
    """
    # For each package id integer in the truck list
    for package_id in truck_list:
        # Get the package object based off of the package id passed into the hash table getter
        package = hash_table.get(package_id)
        # Set the selected package objects hub time to a new hub time
        package.hub_time = hub_time
        # Update the hash table key that matches the package id with the updated package
        hash_table.set(package_id, package)


def update_transit_time(hash_table, truck_list, transit_time):
    """
    update_transit_time:
    The update_transit_time method takes in a hash table, list, and time as arguments. For each package id in the
    list of packages to be delivered, get the specified package out of the hash table, update the time it leaves the hub
    and is in transit with the given transit_time, and set the hash table key to a new value.

    Args:
    hash_table: The hash table is an object reference passed in so the contents can be updated with new transit time
    data.
    truck_list: The truck list is a list of package id's that should have their transit time updated.
    transit_time: The transit time parameter is a time object that updates the current transit time for a package
    object.

    Returns:
    n/a

    Raises:
    n/a

    Algorithmic complexity: O(n). If this hash table had to resize or had more than one element per key, then it could
    be O(n^2), but since we know it does not, then it us O(n). This is due to each element in the truck_list list being
    iterated over.
    """
    # For each package id integer in the truck list
    for package_id in truck_list:
        # Get the package object based off of the package id passed into the hash table getter
        temp_package = hash_table.get(package_id)
        # Set the selected package objects transit time to a new transit time
        temp_package.transit_time = transit_time
        # Update the hash table key that matches the package id with the updated package
        hash_table.set(package_id, temp_package)


def update_delivery_time(hash_table, package_id, delivery_time):
    """
    update_delivery_time:
    The update_delivery_time method takes in a hash table, list, and time as arguments. For the given package id,
    use it to search the hash table for the package object which is held in the value slot, update the package object
    delivery time with the given delivery time, and set the hash table key to a new value (package object).

    Args:
    hash_table: The hash table is an object reference passed in so the contents can be updated with new delivery time
    data.
    package_id: The track list is a list of package id's that should have their transit time updated.
    delivery_time: The delivery time parameter is a time object that is used to update the selected packages delivery
    time.

    Returns:
    n/a

    Raises:
    n/a

    Algorithmic complexity: O(1). At worst case complexity hash table get/sets can be O(n), but happens when there is
    more than one element hashed to the same key, or if the hash table has to be resized. Since we know this hash table
    is 1 to 1 and does not have to be resized (even though it supports chaining), the function ran in this program will
    be O(1).
    """
    # Get a package object based off of a given package id using the hash tables get method
    temp_package = hash_table.get(package_id)
    # Update the packages delivery time with the given delivery time
    temp_package.delivery_time = delivery_time
    # Set the hash table key that matches the package id with the updated package
    hash_table.set(package_id, temp_package)


def update_truck_type(hash_table, truck_list, truck_id):
    """
    miles_to_time:
    The update_truck_type method takes in a hash table, list, and time as arguments. For the given package id,
    use it to search the hash table for the package object which is held in the value slot, update the package object
    truck id with the given truck id, and set the hash table key to a new value.

    Args:
    hash_table: The hash table is an object reference passed in so the contents can be updated with new truck type.
    truck_list: The track list is a list of package id's that should have their truck id updated.
    truck_id: The truck id is the given integer that matches the truck that delivered which package.

    Returns:
    n/a

    Raises:
    n/a

    Algorithmic complexity: O(n). The complexity of the algorithm is O(n) due to each object within a list of objects
    being iterated over. The code within the for loop is O(n) because the get, set, and assignment operations done
    are all O(1) speed.
    """

    for package_id in truck_list:
        temp_package = hash_table.get(package_id)
        temp_package.truck_id = truck_id
        hash_table.set(package_id, temp_package)


def miles_to_time(miles):
    """
    miles_to_time:
    This function takes in an amount of miles, and returns an amount of time based on the speed of the truck,
    and the amount of miles traveled. The speed of a WGUPS truck is 18 miles per hour. 18 MPH = .3 miles/min. The
    converted time is rounded to the nearest minute because there are only 40 packages and more than likely the average
    rounded time lost/gained probably average out.

    Args:
    miles: The miles parameter holds the amount of miles that needs to be converted to a time quantity and object.

    Returns:
    converted_time: Returns an amount of time that has been converted from miles.

    Raises:
    n/a

    Algorithmic complexity: O(1). The algorithm is O(1) because it does a simple dividing operation and applies a
    rounding function to the resulting number, which are both constant.
    """
    # Use the basic equation to convert an amount of miles rounded to an amount of minutes
    converted_time = round(float(miles) / 0.3)
    return converted_time


def add_time(amount_in_minutes, old_time):
    """
    add_time:
    The add_time function takes in a given amount of time in minutes, as well as a time object that needs an amount
    of minutes added to it. It converts the old time into a datetime object, adds the amount_in_minutes quantity to
    the converted_old_date_time, and returns it in the form of a time object.

    Args:
    amount_in_minutes: The amount of minutes parameter holds the amount of minutes that needs to be added to the old
    time.
    old_time: The old_time parameter is the amount of time that needs to be added to so a new time can be created.

    Returns:
    updated_time: The updated_time is a time object that is returned based on the given time and amount of minutes to
    add to that.

    Raises:
    n/a

    Algorithmic complexity: O(1). The complexity of this algorithm is O(1) because most of the code is instantiation and
    assigning values to objects, as well as an addition operation which are all at constant complexity.
    """
    # Non-specific date for conversion use
    temp_date = date.today()
    # Convert separate date and time objects into a datetime object
    converted_old_date_time = datetime.combine(temp_date, old_time)
    # Add the given amount of minutes to the old amount of time, convert that result to a time object, and add that
    # result into a time object
    updated_time = (converted_old_date_time + timedelta(minutes=amount_in_minutes)).time()
    return updated_time


def delivery_algorithm(package_list):
    """
    delivery_algorithm:
    This algorithm is an implementation of the nearest neighbor (greedy) algorithm, starting at the hub address, it goes
    the next closest vertex, and repeats that until every vertex has been visited. After that the algorithm goes back to
    the hub address vertex. The delivery_algorithm accepts a list of packages as one argument to determine which of
    those packages must be delivered first. Organize the list of packages into how they should be delivered (index 0
    first, last index last) and return it in the form of a hash table.

    Args:
    package_list: The package list is a list of integers representing a number of package id's. The package id's are
    are going to be organized throughout the algorithm.

    Returns:
    organized_list: The organized_list is a list of integers that represent package id's that have been organized based
    on an optimally found route of package deliveries.

    Raises:
    n/a

    Algorithmic complexity: O(n^2). This nearest neighbor algorithm is polynomial in time, with a while loop iterating
    over every package id found in a given list, and within that loop a for loop (also) iterates over every package id
    within the package list.
    """
    # Set the hub address to the starting place of all deliveries
    hub_address = "4001 South 700 East"
    current_address = hub_address
    # Create a hash table with all of the package data in it (including their id & address)
    package_table = package_reader()
    # Initialize a dictionary with all of the delivery locations and distances
    distance_dict = distance_reader()
    # Create an empty list that holds the organized package ids
    organized_list = []

    # Start at hud. Each route is a weighted circuit graph where the first and last vertex is the same. With given
    # vertices, determine which circuit has the lowest weight when after evaluation. The vertex of the graph is an
    # address, and the edge is weighted to the amount of miles from one vertex to another.
    while package_list:
        # Create a list to hold package id's from closest to the current_address in the first position
        shortest_list = []
        # Create a float to hold the current shortest distance from the current address
        shortest_distance = None
        # For each package in the package list,
        for package_id in package_list:
            # Get the package info from the package table
            package = package_table.get(int(package_id))
            # Get the distance from the current address to the next address
            distance = distance_dict[current_address][package.address]
            # If shortest distance is not empty...
            if shortest_distance is not None:
                # If the distance is smaller than the shortest found distance from the current location...
                if float(distance) < float(shortest_distance):
                    # Set the distance to the new shortest distance
                    shortest_distance = float(distance)
                    # Append the new shortest distance to the beginning of the shortest list
                    shortest_list.insert(0, int(package.package_id))
                else:
                    # Append the distance to the end of the shortest list as it is not the shortest
                    shortest_list.append(int(package.package_id))
            else:  # Else if the its the first distance access... set shortest distance to distance
                shortest_distance = float(distance)
                # Append the first package to the shortest list to start the list
                shortest_list.append(int(package.package_id))

        # Get the package that holds the address information of the address that was the closest distance
        current_address_package = package_table.get(shortest_list[0])
        # Set the current address to the shortest found address
        current_address = current_address_package.address
        # Append the shortest distance to the end of the organized list
        organized_list.append(shortest_list[0])
        # Remove the first element from the package list
        package_list.remove(shortest_list[0])

    # Returned the organized package list
    return organized_list


