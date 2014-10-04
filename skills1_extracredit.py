# Revision of skills1.py using map/filter/reduce as appropriate.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
f_all_odd = filter(lambda num: num % 2 != 0, number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
f_all_even = filter(lambda num: num % 2 == 0, number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
f_long_words = filter(lambda word: len(word) > 3, word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
f_smallest = reduce(lambda num1, num2: num1 if (num1 < num2) else num2, number_list)

# Write a function that finds the largest element in a list of integers and returns it.
f_largest = reduce(lambda num1, num2: num1 if (num1 > num2) else num2, number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
f_halvesies = map(lambda num: num/2.0, number_list)

def halvesies(number_list):
    newlist = [num/2.0 for num in number_list]
    return newlist

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    newlist = [len(word) for word in word_list]
    return newlist

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total += num
    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    product = 1
    for num in number_list:
        product *= num
    return product

# Write a function that joins all the strings in a list together (without using the join method) and 
# returns a single string.
def join_strings(word_list):
    newstring = ""
    for word in word_list:
        newstring += word
    return newstring

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return sum_numbers(number_list) / float(len(number_list))
