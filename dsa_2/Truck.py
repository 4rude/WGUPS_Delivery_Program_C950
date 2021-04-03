class Truck:
    """The Truck class is used to hold packages to delivery, hold location data about where the truck is at and where
    it should go next, time data about the current time of the truck/driver, and the total mileage of the truck
    objet."""

    # Set the init method for the Truck class so a Truck class can be used to hold truck data, packages, and package
    # statuses
    def __init__(self, truck_id, time, package_list):
        self.truck_id = truck_id
        self.package_list = package_list
        self.time = time
        self.return_time = None
        self.miles = 0.0
        self.current_location = ""
        self.next_location = ""
