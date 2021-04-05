class Package:
    """
    The Package class holds the blueprint for a Package object. The package object represents a package that would be
    used to hold something that needs to be delivered. The kind of data stored here is address information, time
     information, weight information, special notes for the package, and finally a truck id to determine which truck
     the package is being delivered on. A Package object is used in this application to hold data obtained from the
     package_file csv file. The Package object that is created is then added to a hash table for quick access.
    """

    # Set the init method for the Package class so a Package object can be created and hold data
    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, mass, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.special_notes = special_notes
        self.hub_time = None
        self.transit_time = None
        self.delivery_time = None
        self.truck_id = 0
