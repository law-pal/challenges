

# Create a set and loop appen

def match(numlist):
   """
   Function that finds the matching number
   where the second occurrence has the minimal index.
   """
   match = set()
   for number in numlist:
      if number in match:
         return number
      match.add(number)
   return -1


a = [2, 1, 3, 5, 3, 2]
print(match(a))