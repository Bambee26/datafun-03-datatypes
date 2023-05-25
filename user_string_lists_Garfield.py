"""
Author: Bambee Garfield
Course: 44-609-80 Data Analytics Fundamentals Summer OP1 2023
Purpose: Module 3 - Numeric Series

Create and use strings.
"""

import random

from util_datafun_logger import setup_logger

logger, logname = setup_logger(__file__)

    # Task 4. String Lists
    # Work through example_string_lists.py. 
    # Use the example code. 
    # In your user_string_lists.py, using lists of words, terms, teams, categories, or other from your domain.
    # Create about five lists. I'll use listA, listB, etc, but yours should make sense for your domain. 

# Create 5 lists
# Define a list of dog names
list_dog_names = ["Honey", "Venus", "Duke", "Harlow", "Archie", "Venus"]

# Define a list of cat names
list_cat_names = ["Mittens", "Sam", "Bella", "Oliver", "Charlie", "Max", "Bella"]

# Define a list of dog tricks
list_dogs_tricks = ["Sit", "Down", "Stay", "Rollover", "Shake"]

# Define a list of dog breeds
list_dog_breeds = ["Pitbull", "Frenchie", "Great Dane", "Mutt", "German Shepard", "Bulldog"]

# Define a list of cat types
list_cat_types = ["Siamese", "Shorthair", "Persian", "Maine Coon", "Bengal"]


def process_py_functions():
    logger.info(f"String Lists 1. Using Python Built-in Functions ")
    #Use the built-in functions: len(), set(), and zip() to combine 2 or more lists into tuples.
       
    # Get the count and list of words
    dog_ct = len(list_dog_names)

    logger.info(f"There are {dog_ct} dogs on the dog list.")
    logger.info(f"The dogs are {list_dog_names}.")

def create_tuple():
    # Combine two lists into a tuple 
    new_tuple = (list_dog_breeds, list_cat_types)

    logger.info(f"The combined list of dog and cats breeds are: {new_tuple} ")

def create_random_sentence():
    logger.info('\n')
    logger.info(f"String Lists 2. Random Choice")
    
    # Use random.choice() to pick a random value from one of your lists.
    # Customize the sentence generator to create random sentences about your domain. 
    sentence = (f"The dog named {random.choice(list_dog_names)} is a {random.choice(list_dog_breeds)}. "
        f"He's really good at {random.choice(list_dogs_tricks)}. "
        f"Then there is the cat. His name is {random.choice(list_cat_names)} and he is a {random.choice(list_cat_types)}. He does not do tricks.")

    logger.info({sentence})

def process_text():
    #logger.info('\n')
    #logger.info(f"String Lists 3. Get Unique Words")
    # Choose one of the text data files in the repo - or add another related your your domain.
    # Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
    # Sort the list. 
    # Use len() to get the length display it to the console.
    # How good is your list? 

    # read in woodchuck to get a list of words
    with open("text_dogstory.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

    # Get the count and list of words
    word_ct2 = len(list_words)

    logger.info(f"The list of words is: {list_words}")
    logger.info(f"There are {word_ct2} words in the file.")

    # Print the count and list of unique words
    unique_word_ct = len(unique_words)

    logger.info(f"The set of unique words is: {unique_words}")
    logger.info(f"There are {unique_word_ct} unique words in the file.")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    process_py_functions()
    create_tuple()
    create_random_sentence()
    process_text()
  
    show_log()
