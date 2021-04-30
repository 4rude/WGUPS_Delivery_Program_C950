# WGUPS_Delivery_Program_C950
A delivery program written for a final project for Data Structures and Algorithms 2 for the Computer Science program with WGU.

ALGORITHM SELECTION 
The self-adjusting algorithm used to determine what order/when the packages should be delivered was a greedy/nearest-neighbor algorithm. The algorithm takes a list of packages that are meant for a specific truck and organizes them based on their distance from the hub address and previous address. The list of packages is manually built based on what time and what area they need to be delivered, and then the list is passed into the nearest-neighbor algorithm. The algorithm sets the first/current address as the hub of WGUPS and then determines which address must be visited based on the weights of the other addresses in the list of packages that the truck must deliver. The fact that the algorithm decides which addresses must be visited from a given list of addresses means it is self-adjusting. The algorithm knows that the first and last address must be the hub address (as the truck must leave and return the WGUPS hub), but other than that it calculates an optimal route using the weights of the next addresses (to be visited) concerning the current address. To determine which route should be taken, the algorithm looks at the hub address, sets it to the current address, checks each other address in the list of addresses that must-have packages delivered to them, goes to the closest, sets that address to the current address, and then does the same until all of the packages are delivered after which it returns to the hub.

SOFTWARE EFFICIENCY AND MAINTAINABILITY
The algorithm used to determine what route the trucks must take, as well as the rest of the algorithm that delivers the packages, is all efficient and in polynomial time. The space-time complexity of the entire application never runs worse than O(n3) complexity, and this is found in the CLI module that runs the user interface. The nearest-neighbor algorithm used to determine what route the truck must take to deliver the packages runs at O(n2) in the worst-case, which is considered efficient. 

The code is very maintainable because it uses encapsulation to clearly define how each part of the solution is created, has a clear code structure that is simple and easy for any programmer to understand, and also if very well commented out (nearly every line is commented) and each function has an accompanying docstring. The encapsulation is done by creating a module that either defines a class to helps create objects or holds several functions that are related to the module name. The code structure in this application helps with maintainability because classes are created to represent things that would intuitively be used in a delivery program like this (Package, Truck, HashTable) and the module names and function names define what kind of behavior is expected to be found throughout the application. Finally, the program has a comment before nearly every line of code that explains what will be happening below it, so programmers can understand the flow of data and logic which creates the solution. Also, each function has a docstring below it, so it defines the name of the function, a description, its arguments, what it returns, and finally its algorithmic complexity.

SELF-ADJUSTING DATA STRUCTURES
The WGUPS delivery application includes a custom-written self-adjusting hash table data structure. This data structure is useful for this application because it is used to hold package objects that can be inserted, created, and deleted in O(1) worst-case complexity. One of the strengths of writing a custom hash table, and using a hash table in general, is the fact that the hash function can be written with the number of keys that will be used in mind. In this case, the hash table holds 40 packages each with a distinct package id. Since we know that there will only be 40 packages used, we can write a simple hash function that will map each key to its bucket, removing the need for the hash table to adjust or be accessed slower than O(1) time. With that being said, the hash table is self-adjusting by using chaining to add keys to buckets that it collides with. This is another strength because the hash table can scale to more packages. 

A weakness of this hash table also lies in the hash function. The hash function takes the package id finds the modulo of that and the table size (which is static at the integer 40) and uses that result to find the key of the bucket that stores the key-value pair, or object. The disadvantage of this is that it will not evenly spread out the package ids if more than forty packages are being stored in the hash table. If that occurs, the get and set complexities could increase to O(n) access times. Another weakness is the fact that the hash table (in its current form) cannot be easily iterated over like a list can, possibly making the code harder to read for future programmers that need to maintain it.

DEVELOPMENT ENVIRONMENT
The programming language used to create this application is Python. The interpreter used to process the program is Python 3.7. The IDE used to write, debug, and test the program is PyCharm 2020.2.3. The operating system that ran PyCharm when making this application is macOS Catalina Version 10.15.4. The hardware used to write the application, run PyCharm, and run interpreter on MacBook Pro 2017. 
