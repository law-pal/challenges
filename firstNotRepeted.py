from collections import Counter

def first_not_repeating_character(string):
   """
   Function to find the first non repeted character in a string of english letters
   """
   counter = Counter(string)
   for key, value in counter.items():
      if value <= 1:
         return key
         break
   return '_'



s = "abacabad"
print(first_not_repeating_character(s))

