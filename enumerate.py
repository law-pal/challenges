from collections import Counter

string = 'enumerate an Iterable'

def retrieve_char(string):
   """
   Function that puts a string into a dictionary
   storing the indices of a repeated letter in a lists 
   as values and the letters as keys.
   """
   char_indices = dict()
   for index, char in enumerate(string):
      if char in char_indices:
         char_indices[char].append(index)
      else:
         char_indices[char] = [index]
   return char_indices


