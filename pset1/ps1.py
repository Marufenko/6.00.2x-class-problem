###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result_list = []
    sorted_cows = sorted(cows.items(), key = lambda x: x[1],reverse = True) 
    
    #total_weight will be used to check if all cows are loaded into vehicles
    used_list = []
    total_weight = 0
    for i in range(len(sorted_cows)):
        total_weight += sorted_cows[i][1]

    test_weight = 0
    
    while test_weight != total_weight: #when total loaded mass will be equal to total_weight - we finish calculation
        limit_cargo = 0
        result = []
        for i in range(len(sorted_cows)):
            if sorted_cows[i][0] not in used_list:
                if sorted_cows[i][1] + limit_cargo <= limit:
                    result.append(sorted_cows[i][0])
                    used_list.append(sorted_cows[i][0])
                    limit_cargo += sorted_cows[i][1]
                    test_weight += sorted_cows[i][1]
        result_list.append(result)
        
    return result_list


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    test_dict = []
    for cow in (get_partitions(cows)):
        test = []
        for items in cow:
            total_weight = 0
            for item in items:
                total_weight += cows[item]
            if total_weight <= limit:
                test.append(1)
            else:
                test.append(0)
        if 0 not in test:
            test_dict.append([cow,len(test)])
    result = 1000
    for element in test_dict:
        if element[1] < result:
            result = element[1] # result will contains len of the shortest list
    for element in test_dict:
        if element[1] == result:
            return element[0]
                
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    print(brute_force_cow_transport(cows, 10))
    end = time.time()
    return (end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("C:\ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

print(brute_force_cow_transport({'MooMoo': 50, 'Boo': 20, 'Miss Bella': 25, 'Horns': 25, 'Milkshake': 40, 'Lotus': 40}, 100))

compare_cow_transport_algorithms()
