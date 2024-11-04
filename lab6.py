import data
from typing import Optional
from data import Book

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None
    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex

# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1: A selection sort algorithm that sorts an inputted list of books by title in alphabetical order
#Parameters:
# books (list[Book]): The book we want to sort

#Returns: The sorted inputted list is returned in alphabetical order
def selection_sort_books(books: list[Book]) -> None:
    for i in range(len(books) - 1):
        min_idx = i
        for j in range(i + 1, len(books)):  # finding the smallest
            if books[j].title < books[min_idx].title:
                min_idx = j
        if min_idx != i:  # for your swapping
            temp = books[i]
            books[i] = books[min_idx]
            books[min_idx] = temp

# Part 2: A function that takes a string and swaps the uppercase letters with lowercase letters and vice versa
#Parameters:
# input_str: the string that we want to manipulate

#Returns: The inputted string but with the lowercase letters now uppercase and the uppercase letters now lowercase
def swap_case(input_str: str) -> str:
    swapped = ""
    for char in input_str:
        if char.isupper():
            swapped += char.lower()
        elif char.islower():
            swapped += char.upper()
        else:
            swapped += char
    return swapped

# Part 3: A function that takes a string and swaps the specified string with a new string
#Parameters
# input_str: the string that we want to manipulate
# old_char: the character (data type str) that we want to swap with the new character
# new_char: the character (data type str) that we will swap with the old character

#Returns: The inputted string with the old_char replaced with new_char
def str_translate(input_str: str, old_char: str, new_char: str) -> str:
    new_str = ''
    for char in input_str:
        if char == old_char:
            new_str += new_char
        else:
            new_str += char
    return new_str

# Part 4: A function that takes a string and returns a dictionary mapping each word in the string to an integer

#Parameters
# input_strings: the inputted string that will be split and whos individual strings will be added to the dictionary

#Returns: A dictionary with each word in the input_strings mapped to a count of the number of times the word appears in input_strings
def histogram(input_strings: str):
    input_strings_split = input_strings.lower().split()
    dictionary = {}
    for strings in input_strings_split:
        if strings in dictionary:
            dictionary[strings] += 1
        else:
            dictionary[strings] = 1
    return dictionary