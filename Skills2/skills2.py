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
# Took 4 minutes.
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
	    
#print count_unique("twain.txt")

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
# Took 10 minutes
def common_items(list1, list2):
    set1, set2 = set(list1), set(list2)
    common_set = set1.intersection(set2)
    common_list = list(common_set)
    return common_list

# print common_items(list1, list2)

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
# Took 45 minutes
def common_items2(list1, list2):
    d = {}

    # Look for each list1 item in d. If it's already a key, do nothing. 
    # If it's not there, create it and give it a value of 1.
    for item in list1:
        d[item] = d.get(item, 1)
    
    # Look for each list2 item in d. 
    # If it's already a key, add 1 to its value. Otherwise give it a 0 value.
    for item in list2:
        d[item] = d.setdefault(item, 0) + 1

    common_list = []

    for key, value in d.iteritems():
        if value == 2:
            common_list.append(key)

    return common_list

# print common_items2(list1, list2)
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
# Took 7 minutes
def sum_zero(list1):

    d = {}

    for num in list1:
        if num * -1 in list1:
            d[num] = d.get(num, 0)
    return d.keys()

#print sum_zero(list1)



"""
Given a list of words, return a list of words with duplicates removed
"""
# Took 2 minutes
def find_duplicates(words):

    d ={}
    
    for word in words:
        d[word] = d.get(word, 0)

    return d.keys()

# print find_duplicates(words)
"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
# Started at 4:25
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
print the sentence translated to pirate.
"""