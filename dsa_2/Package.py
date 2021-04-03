class Package:
    """The Package class holds the blueprint for a Package object. A Package object is used to hold data obtained
    from the package_file csv file. The Package object can then be added to a hash table for quick access."""

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
