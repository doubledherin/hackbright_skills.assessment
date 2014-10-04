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

# Write a function that takes a list of words and returns a list of all the lengths of those words.
f_word_lengths = map(lambda word: len(word), word_list)

# Write a function (using iteration) that sums all the numbers in a list.
f_sum_numbers = reduce(lambda num1, num2: num1 + num2, number_list)

# Write a function that multiplies all the numbers in a list together.
f_mult_numbers = reduce(lambda num1, num2: num1 * num2, number_list)

# Write a function that joins all the strings in a list together (without using the join method) and 
# returns a single string.
f_join_strings = reduce(lambda word1, word2: word1 + word2, word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return sum_numbers(number_list) / float(len(number_list))
