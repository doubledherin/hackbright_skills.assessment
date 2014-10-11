import string

string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
# Done in 4 minutes.
def count_unique(string1):
    # Split string into list of words
    wordlist = string1.split()

    # Initialize an empty dictionary
    hist = {}

    # Iterate over list of words and check to see if each word is in the dictionary. 
    # If it's not, add it and increment count.
    for word in words:
    	hist[word] = hist.get(word, 0) + 1
    return hist

#print count_unique(string1)

# Bonus (using a file)
# Took like 30 minutes because of a Sublime problem
def count_unique(filename):
    # Open file and read it in line by line
    fin = open(filename)

    # Initialize an empty dictionary
    hist = {}

    # Iterate over list of words and check to see if each word is in the dictionary. 
    # If it's not, add it and increment count.
    for line in fin:
        line = line.replace("-", " ")
     	words = line.lower().split()
     	for word in words:
            word = word.strip(string.punctuation)
        hist[word] = hist.get(word, 0) + 1

    return hist

	    
#print count_unique(string1)
print count_unique("twain.txt")

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    pass

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    pass

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    pass

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""