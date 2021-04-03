# First Name: Matthew, Last Name: Rude, Student ID: #001260851
from CLI import *

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Main function that runs the project
if __name__ == '__main__':

    # Create a user_input loop to act as a command line interface
    while True:
        user_input = input("Please enter a valid time in military time format ie. '1600' or enter 'X' to end the "
                           "program.")

        # If user input is x, end the application.
        if user_input == "X" or user_input == "x":
            print("Program closed.")
            break
        # If the user input is a valid military time... process the time and return package/delivery info
        elif validate_input(user_input):
            process_time(user_input)

    """ 
    hash_table = HashTable()

    hash_table.set(1, "goodbye")
    hash_table.set(40, "where")
    hash_table.set(40, "hello")

    hash_table.print_hash_table()
    
    # Test Packages
    p1 = Package(1, "22 Street", "City" "State", 23845, "10:30AM", "10lb", "none", "what")
    p2 = Package(2, "22 Street", "City" "State", 23845, "10:30AM", "10lb", "none", "what")

    test_dict = {p1.package_id: p1, p2.package_id: p2}
    test_hash_table = HashTable()

    for key, value in test_dict.items():
        test_hash_table.set(key, value)
    

    package_hash_table = package_reader()
    distance_dict = distance_reader()

    print(json.dumps(distance_dict, indent=4))

    hash_table = HashTable()

    hash_table.set(1, "goodbye")
    hash_table.set(41, "why")
    hash_table.set(40, "yellow")
    hash_table.set(40, "hello")

    hash_table.print_hash_table()
    
    package_hash_table.print_hash_table()
    

    truck_one_list = [1, 2, 3]
    truck_one = Truck(1, time(8, 0), truck_one_list)
    for p in truck_one.package_list:
        print(p)

    while truck_one.package_list:
        truck_one.package_list.pop(0)

    if not truck_one.package_list:
        print("empty")
    
    # Test Packages
    p1 = Package(1, "22 Street", "City" "State", 23845, "10:30AM", "10lb", "none", "what")
    p2 = Package(2, "22 Street", "City" "State", 23845, "10:30AM", "10lb", "none", "what")
    p1.delivery_time = time(8, 0)

    print(p1.delivery_time)

    hash_table = HashTable()
    hash_table.set(p1.package_id, p1)
    hash_table.set(p1.package_id, p2)

    package = hash_table.get(1)

    package.delivery_time = time(9, 0)
    print(package.delivery_time)
    hash_table.set(1, package)

    hash_table.print_hash_table()

    package_test = hash_table.get(1)
    print("Package test ", package_test.delivery_time)
    
    packages = package_reader()
    packages.print_hash_table()
    test_package = packages.get(2)
    print("TEST PLS WORK", test_package.address)
    
    # MILE CONVERSION TEST 
    converted_miles = miles_to_time(14.1)

    new_time = time(8, 0)

    added_time = add_time(converted_miles, new_time)
    print(added_time)
    
    
    package_hash_table = deliver_packages()
    # distance_dict = distance_reader()

    # print(distance_dict["1330 2100 S"].items())


    print("----------------------------")
    #  delivery_algorithm_two()
    
    before_time = time(8, 0)
    after_time = time(10, 0)
    if before_time < after_time:
        print("We good")
    """