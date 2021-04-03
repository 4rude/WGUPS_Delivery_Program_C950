import csv  # Import the CSV python library
from Package import *  # Import the Package class to create package objects
from HashTable import *


def package_reader():
    """
        package_reader:
        The package_reader function takes in a csv file url as an argument, and returns a dictionary filled with
        organized csv data.

        Args:
        n/a

        Returns:
        package_hash_table:

        Raises:
        n/a

        Algorithmic complexity: O(n).
        """
    # Open the package_file so it can be accessed using the csv library
    with open("resources/package_file.csv") as file:
        # Create a list filled with CSV data
        read_csv = csv.reader(file, delimiter=",")

        # Create a dictionary to hold package objects
        package_hash_table = HashTable()

        # For each row in the read_csv list...
        for row in read_csv:
            # Create a package object and fill it with data from the read_csv list
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            # Add the package object to the package_dictionary, cast package_id as an integer so it can be used as a
            # key in the hash table
            package_hash_table.set(int(package.package_id), package)

        return package_hash_table

