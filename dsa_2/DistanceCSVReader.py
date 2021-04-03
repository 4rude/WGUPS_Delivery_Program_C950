import csv  # Import the CSV python library


def distance_reader():
    """
    distance_reader:
    The distance_reader function takes in a csv file url as an argument, and returns a dictionary filled with
    organized csv data.

    Args:
    n/a

    Returns:
    all_distances_dict:

    Raises:
    n/a

    Algorithmic complexity: O(n^2).
    """
    # Open the distance_table so it can be accessed using the csv library
    with open("resources/distance_table.csv") as file:
        # Create a list filled with CSV data
        read_csv = csv.reader(file, delimiter=",")

        # Create a list of street names from the csv file
        csv_list = list(read_csv)

        street_list = csv_list[0]

        # Create a dictionary to hold dictionaries that hold streets and their distances apart
        all_distances_dict = {}

        # For each row in the csv list, skipping the first row...
        for row in csv_list[1:]:
            # Create a temporary dictionary to hold key/value pairs of street & distance
            temp_dict = {}
            for i in range(1, 28):
                # Add key of row[0] and value of row[i] to temp_dict
                temp_dict[street_list[i]] = float(row[i])
            # Add temp_dict as value of row (address) key
            all_distances_dict[row[0]] = temp_dict

            # print(row)

        # Return the all_distances dictionary
        return all_distances_dict
