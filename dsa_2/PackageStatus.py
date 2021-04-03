import datetime


class PackageStatus:
    """The PackageStatus class is used to hold time information about a packages delivery. It holds the package and
     package address, the time it started its day in the hub, """

    # Set the init method for the Package Status class so it can hold delivery data about a package.
    def __init__(self, package_id, current_status):
        self.package_id = package_id
        self.current_status = current_status
        self.hub_time = datetime.time(8, 0)
        self.transit_time = datetime.time(8, 0)
        self.delivery_time = datetime.time(8, 0)
