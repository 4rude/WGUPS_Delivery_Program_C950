class HashTable:
    """
    Class HashTable:
    This is a custom Hash Table designed to create an object that holds data in the key/value pair form. The
    Hash Table runs fast due to it being from O(1) to O(n) access time (and in this application, due to the amount of
    objects that we know will be held in this hash table, it will be O(1) access time).
    """

    def __init__(self):
        # Initialize the amount of buckets in the hash table
        self.table_size = 40
        # Initialize the hash table with table_size amount of buckets
        self.table = [None] * self.table_size

    def set(self, key, value):
        """
        The set() function sets a key and value to an entry in the Hash Table depending on the keys hashed value.
        The set function also adds chaining to the hash table. It does this by looking at each sub-list in the
        bucket, re-setting its value to the given value (in the argument) if the key already exists, and adding a new
        sub-list to the bucket if the key does not already exist. This chaining functionality to the set function
        of the hash table qualifies for the self-adjusting requirement.

        Algorithmic complexity: O(1).
        """
        # Hash the given key to determine where to place the key/value pair
        hashed_key = self._hash_algorithm(key)
        # Create a list with the key & value held in it
        hashed_value = [key, value]

        # If the bucket is empty
        if self.table[hashed_key] is None:
            # Add a two value list to the table index of the hashed key
            self.table[hashed_key] = list([hashed_value])
            return True
        else:  # If bucket is not empty
            # For each pair in the bucket found...
            for pair in self.table[hashed_key]:
                # If the key/value pair exists... return True
                if pair[0] == key:
                    pair[1] = value
                    return True
            # If the key/value pair does not exist, append it to the bucket
            self.table[hashed_key].append(hashed_value)
            return True

    def get(self, key):
        """
        The get() function returns a value of an entry matching the given key within the hash table.

        Algorithmic complexity: O(1).
        """
        # Create a hashed key based off of the input for the key
        hashed_key = self._hash_algorithm(key)

        # If bucket matching the hashed key is not empty...
        if self.table[hashed_key] is not None:
            # For each entry in the hash_table...
            for pair in self.table[hashed_key]:
                # If the first index of the entry equals the key
                if pair[0] == key:
                    # Return the value
                    return pair[1]

    def delete(self, key):
        """
        The delete() function removes a table entry matching the given key within the hash table.

        Algorithmic complexity: O(1).
        """
        # Create a hashed key based off of the input for the key
        hashed_key = self._hash_algorithm(key)

        # If the entry for the given key if empty...
        if self.table[hashed_key] is None:
            return False
        # For each element in the range from zero to the size of the table...
        for i in range(0, len(self.table[hashed_key])):
            # If the entry of the table matches the given key...
            if self.table[hashed_key][i][0] == key:
                # Delete the matching table entry
                self.table[hashed_key].pop(i)
                return True

    def print_hash_table(self):
        """
        The print_hash_table() prints out each entry in the Hash Table to the command line interface.

        Algorithmic complexity: O(n).
        """
        print("---------HASH TABLE----------")
        # For each entry in the hash table...
        for entry in self.table:
            # If the entry is not empty...
            if entry is not None:
                print(str(entry))

    def _hash_algorithm(self, key):
        """
        The _hash_algorithm is a very simple algorithm that hashes a number and returns it. It calculates the
        key given modulo the size of the table. This is a 1-1 mapping because it is known that there are only
        40 unique keys that will be used, so we only need to generate 40 buckets (which is the most efficient method
        when a user knows the amount of data that a hash table will hold.

        Algorithmic complexity: O(1).
        """
        return int(key) % self.table_size
