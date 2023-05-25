"""
Author: BAmbee Garfield
Course: 44-609-80 Data Analytics Fundamentals Summer OP1 2023
Purpose: Module 3 - Numeric Series

Create and use lists.

"""

# import from standard library
import statistics
import math

# import from local files
from util_datafun_logger import setup_logger

# Set up logging .............................................

# Call the setup_logger function
logger, logname = setup_logger(__file__)

# Define shared data ..........................................

# define a variable with some univariant data
# weight of Sparky the dog over last 24 months (he's a large dog)
list_1 = [96, 97, 96, 94, 96, 97, 99, 95, 96, 93, 99, 100, 99, 97, 98, 99, 96, 95, 94, 94, 95, 93, 94, 93]

# univariant time series data (one varabile over time)
# x = month of year
# y = days in each month
list_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
list_y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Define functions ........................................


def list_statitics():
    """This function illustrates descriptive statistics for a numeric list."""

    logger.info(f"Lists 1. List Statistics")
    # Calculate the mean, median, and mode (hint: import statistics module)
    # Calculate the standard deviation and variance 

    logger.info(f"The list of Sparky's weights is: {list_1}.")

    mean = statistics.mean(list_1)
    median = statistics.median(list_1)
    mode = statistics.mode(list_1)

    logger.info(f"The mean or average of Sparky's weights over the last 24 months is: {mean:.2f}.")
    logger.info(f"The median or middle value of Sparky's weights over the last 24 months is: {median:.2f}.")
    logger.info(f"The mode or most commonly occuring of Sparky's weights is: {mode}.")

    stdev = statistics.stdev(list_1)
    variance = statistics.variance(list_1)

    logger.info(f"The standard deviation of Sparky's weights is: {stdev:.2f}.")
    logger.info(f"The variance (or squared differences from the mean) of Sparky's weights is: {variance:.2f}.")


def list_correlation_prediction():
    """This function illustrates correlation and prediction for a numeric list."""
    logger.info('\n')
    logger.info(f"Lists 2. Lists - Correlation and Prediction")
    # Calculate the correlation between listx and listy
    # Calculate the slope and intercept of the best fit line. Hint: use statistics.linear_regression()
    # Set a future time = 15. 
    # Predict the y value at the future time  y = mx + b where m is the slope and b is the y intercept
   
    logger.info(f"X is the list of months. It is: {list_x}.")
    logger.info(f"Y are the number of days in each month. It is: {list_y}.")

    correlationxy = statistics.correlation(list_x, list_y)
    logger.info(f"The correlation between x and y is {correlationxy:.2f}.")

    slope, intercept = statistics.linear_regression(list_x, list_y)
    logger.info(f"The equation of the best fit line is: y = {slope:.2f}x + {intercept:.2f}.")

    x_max = max(list_x)
    newx = x_max * 15  # predict for a future x value

    newy = slope * newx + intercept

    logger.info(f"We predict that when x = {newx:.2f}, y will be about {newy:.2f}.")


def list_built_in_functions():
    logger.info('\n')
    logger.info(f"Lists 3. Lists - Using Python Built-in Functions")
    # min()
    # max()
    # len()
    # sum()
    # average (hint use two values already calculated)
    # set()
    # sorted()
    max_value = max(list_1)
    min_value = min(list_1)
 
    # min
    logger.info(f"The highest Sparky's weight was: {max_value}.")
    
    # max
    logger.info(f"The lowest Sparky weighed was: {min_value}.")

    # len
    len_list = len(list_1)
    logger.info(f"There are {len_list} number of weigh-ins on this list.")

    # sum
    sum_list = sum(list_1)
    logger.info(f"If we add all of Sparky's weigh-ins together, the sum is {sum_list}.")

    # average
    avg_list = sum_list / len_list
    logger.info(f"Over the last 24 months, Sparky's average weight was {avg_list:.2f}.")

    # set
    sparky_goal_weight = {94, "lbs"}
    logger.info(f"Sparky's goal weight: {sparky_goal_weight}")
    
    # sort (ascending and descending)
    asc_weights = sorted(list_1)
    desc_weights = sorted(list_1, reverse=True)

    logger.info(f"If we sort all of Sparky's weights in order from lowest to highest: {asc_weights}.")
    logger.info(f"If we sort the weights from highest to lowest: {desc_weights}.")


def list_methods():
    logger.info('\n')
    logger.info(f"Lists 4. List Methods")
    # Make a new short list named lst and explore list methods: 
    #
    # append() a single value to the list
    # extend() the list with a new list you pass in
    # insert() at an index, insert a value
    # remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
    # count(2) count how many times 2 appears in your list (if it doesn't, change  2 to a value in your list)
    # sort()
    # sort(), with reverse=True to get them in descending order
    # copy()
    # pop() the first item off the top of the list/stack
    # pop() the last time off the bottom of the list/stack

    # append() a single value to the list
    list_x
    list_x.append(13)
    logger.info(f"If we append our month's list with 13, we get {list_x}.")

    # extend() the list with a new list you pass in
    list_x.extend([14, 15, 16])
    logger.info(f"We can also combine that list with a new list of 14, 15 and 16 to get: {list_x}.")

    # insert() at an index, insert a value
    i = 0
    newvalue = 42
    list_x.insert(i, newvalue)
    logger.info(f"We can insert a new value of 42 to the list to get {list_x}.")

    # remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
    item_to_remove = 42
    list_x.remove(item_to_remove)
    logger.info(f"Now we'll remove the 42 because it doesn't fit this list and we get: {list_x}.")

    # count(2) count how many times 2 appears in your list (if it doesn't, change 2 to a value in your list)
    ct_of_97 = list_1.count(97)
    logger.info(f"Back to Sparky's list. The number 97 appears in the weight list {ct_of_97} times.")

    # sort()
    asc_scores = list_1.sort()
    logger.info(f"The weights in ascending order are {asc_scores}.")

    # sort(), with reverse=True to get them in descending order
    desc_scores = list_1.sort(reverse=True)
    logger.info(f"The weights in descending order are {desc_scores}.")

    # copy ()
    new_weights = list_1.copy()
    logger.info(f"Sparky's new weight list is: {new_weights}.")

    # pop() the first item off the top of the list/stack
    first = new_weights.pop(0)
    logger.info(f"Popped the first (index=0): {first} and now, the weights are: {new_weights}.")

    # pop() the last item off the top of the list/stack
    last = new_weights.pop(-1)
    logger.info(f"Popped the last item: {last} and now, the weights are: {new_weights}.")


def list_transformations():
    logger.info('\n')
    logger.info(f"Lists 5. List Transformations - Using filter() and map()")
    # Transformation - filter() and map() - critical for big data processes that must scale!

    # Use the built in filter() function to keep x such that x is less than 4 (or some other cutoff), or keep the even ones, whatever.
    # Use the built in map() function to map each x to cuberoot of x (hint: use math module)
    # Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. Hint: Volume = side * side * side
    
    # Use the built in filter() function to keep x such that x is less than 4 (or some other cutoff), or keep the even ones, whatever.
    weights_over_97 = list(filter(lambda x: (x > 97), list_1))
    logger.info(f"These were Sparky's weigh-ins over 97 lbs: {weights_over_97}.")

    # Use the built in map() function to map each x to cuberoot of x (hint: use math module)
    cuberoot_weights = list(map(lambda x: (round(x ** (1/3), ndigits=2)), list_1))
    logger.info(f"If we take the cube root of each weigh in, we get: {cuberoot_weights}")

    # Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. Hint: Volume = side * side * side
    cube_vol = list(map(lambda x: (x * x * x), list_y))
    logger.info(f"Using the numbers of days each month (list_y) as side lengths, calulate the volume of a cube: {cube_vol}")


def list_comprehensions():
    logger.info('\n')
    logger.info(f"Lists 6. List Transformations - Using List Comprehension")
    # Comprehension means to "grasp together" 
    # Or to use one list to "completely describe" a new list
    # Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff. 
    # Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 
    # Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.
    
    # Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff.
    weights_under_97 = [x for x in list_1 if x < 97]
    logger.info(f"Sparky's weigh-ins that were under 97 lbs: {weights_under_97}")

    # Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 
    triple_weights = [x * 3 for x in list_1]
    logger.info(f"Sparky's weigh-ins tripled: {triple_weights}")

    # Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.
    sqrt_weights = [round(math.sqrt(x), ndigits = 2) for x in list_1]
    logger.info(f"Square roots of Sparky's weigh-ins: {sqrt_weights}.")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
if __name__ == "__main__":
    logger.info("Project 3 - Numeric Lists ")

    # call your functions here (see instructions)
    list_statitics()
    list_correlation_prediction()
    list_built_in_functions()
    list_methods()
    list_transformations()
    list_comprehensions()

    show_log()
