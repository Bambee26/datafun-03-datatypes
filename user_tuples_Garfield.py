"""
Author: Bambee Garfield
Course: 44-609-80 Data Analytics Fundamentals Summer OP1 2023
Purpose: Module 3 - Numeric Series

"""
# Task 5.  Tuples and More
# Work through example_tuples_etc.py. 
# Use the example code. 
# Use your file, user_tuples_etc.py to practice with tuples, sets, and dictionaries in your domain. 
# Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples.
# Sets: create two sets. Get the intersection and the union.
# Dictionaries: See the examples. 
# Use a dictionary to create key-value pairs of each word and its count from a file. 
# See the example file. Using a loop is okay, but the true Python approach is a dictionary comprehension (fully defining how to build a dict from a list in one short line of code. 


# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


def illustrate_tuples():
    """This function illustrates tuples in Python."""
    logger.info(f"EXAMPLES OF TUPLES")
    
    # Create some tuples
    tupleA = (12, 23, 34, 45, 56)
    tupleB = (49, 58, 67, 76, 85)

    # tuple concatenation
    tupleCat = tupleA + tupleB

    # tuple repetition
    tupleAThrice = tupleA * 3

    # TODO: Start using this f-string "syntactic sugar" for quick ouptut
    # just add space = space inside the curly braces
    # it will print the name of the variable and the value
    logger.info(f"Tuple A = {tupleA}")
    logger.info(f"Tuple B = {tupleB}")
    logger.info(f"Tuples concatenated = {tupleCat}")
    logger.info(f"Tuple A times 3 = {tupleAThrice}")

    # tuple membership testing

    tupleD = (1, 2, 3)
    hasOne = 1 in tupleD  # True
    hasFour = 4 in tupleD  # False

    logger.info('\n')
    logger.info(f"TESTING TUPLES")
    logger.info(f"Testing tuple membership with True: {hasOne}")
    logger.info(f"Testing tuple membership with False: {hasFour}")
   
    # tuple indexing (0 is first, -1 is last, or 1 less than the length)

    my_tuple = (1, 2, 3)
    first = my_tuple[0]
    second = my_tuple[1]
    third = my_tuple[2]
    last = my_tuple[-1]

    logger.info(f"My test tuple {my_tuple}")
    logger.info(f"Testing tuple indexing: {first}, {second}, {third}, {last}")

    # Use tuples to return multiple values from a function

    def divide_and_remainder(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

    q, r = divide_and_remainder(10, 3)
    logger.info(f"Quotient: {q}, Remainder: {r}")


def illustrate_sets():
    """This function illustrates sets in Python."""

    setA = {1, 2, 3, 4, 5}
    setB = {4, 5, 6, 7, 8}

    logger.info(f"setA = {setA}")
    logger.info(f"setB = {setB}")

    # set union
    setC = setA | setB

    # set intersection
    setD = setA & setB

    # set difference
    setE = setA - setB

    # sets are often used to remove duplicates from a list
    # after gettin the set, convert it back to a list with list() or []
    listWords = ["apple", "banana", "apple", "pear", "banana", "orange"]
    setWords = set(listWords)
    listWordsNoDuplicates = list(setWords)
    listWordsNoDuplicates = [setWords]  # same as above


def illustrate_dictionaries():
    """This function illustrates dictionaries in Python."""

    dogA_dict = {"name": "Rex", "age": 2, "weight_kg": 13.4}
    dogB_dict = {"name": "Fido", "age": 3, "weight_kg": 15.2}

    logger.info(f"dogA_dict = {dogA_dict}")
    logger.info(f"dogB_dict = {dogB_dict}")

    assessment_dict = {"low": 0, "medium": 1, "high": 2}
    logger.info(f"assessment_dict = {assessment_dict}")

    data_dict = {
        "name": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, 35, 40],
        "income": [50000, 60000, 70000, 80000],
    }
    logger.info(f"data_dict = {data_dict}")

    """# In data anlytics, dictionaries may be used to store and manipulate
    # tabular data, e.g. from database records or Excel rows.

    # Dictionaries can be used to store and aggregate statistical data,
    # such as counts or sums. For example, a dictionary of word-count pairs.

    with open("text_simple.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info("Word count is a good way to begin processing text.")
    logger.info(f"Given text_simple.txt, the word_counts_dict = {word_counts_dict}")

    # IMPORTANT: Dictionary comprehesions - the preferred approach

    # Create a dictionary of word counts from a list of words
    # A dictionary is always key:value pairs
    # Say "I want word:count for each word in word_list"
    # Cast the result to a dictionary by using curly braces {}
    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    # Spend most of your practice on comprehensions - they are
    # key to transforming data in Python.

    logger.info("Given text_simple.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")"""


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")
    show_log()
