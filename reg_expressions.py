# https://regexr.com/

# for basic matching, don't use regular expressions. they are for complex searches

# Metacharacters in regular expressions
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs

import re
text='''Technology is the application of conceptual knowledge for achieving practical
 goals, especially in a reproducible way.The word technology can also mean the 
 products resulting from such efforts, including both tangible tools such as 
 utensils or machines, and intangible ones such as software. Technology plays a 
 critical role in science, engineering, and everyday life.'''
pattern="[A-Z]ech"
# print(re.search(pattern,text)) #span=(0, 4), match='Tech' span ka matlan y h k
# 'tech' ka word 0th index s start hua or 4-1th index pr khtam hua

# This method stops after the first match, so this is best suited for testing a regular
#  expression more than extracting data. 

#  !!!!!!!!!!!!!!  re.findall()  !!!!!!!!!!!!!!!!!!!!!!!!!!!
pattern="[A-Z]ech"
# print(re.findall(pattern,text)) #re.findall function to find all occurrences of the
# pattern in a string:

# !!!!!!!!!!!!!!!!!!!!!  re.sub()  !!!!!!!!!!!!!!!!!!!!
import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
# Output: ['cat', 'hat']
new_text = re.sub(pattern, "dog", text)
print(new_text)
# Output: "The dog is in the dog."
#  !!!!!!!!!!!!!!  shows how to extract information from a string using regular expressions:



# PRACTICE:
textt='''Python is a versaatile dersat ersat dersati programming language known for its simplicity and readability. 
It is widely used in web development, data analysis, artificial intelligence, and scientific computing.
Regular expressions (regex) are powerful tools for pattern matching and text search in Python.
They provide a concise and flexible means for identifying specific patterns within strings.
Using regex, you can efficiently search for words, numbers, dates, email addresses, and more in text data.
'''
patternn="\w?ersa\w?\w(ile)?"
print(re.findall(patternn,textt)) 