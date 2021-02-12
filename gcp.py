
def gcd(a, b):
   """
   Function that finds the Greatest Common Divisor between two numbers
   """
   while b != 0:
      temp_a = a
      a = b
      b = temp_a % b   
   return a
   
# Creates a list of tuples defining pairs of coprime numbers
# list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
# list2 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
# coprimes = [(i, j) for i in list1 for j in list2 if gcd(i, j) == 1]
# print(coprimes)


# Take strings s1, s2 and list their common characters
common_chars = lambda s1, s2,: set(s1).intersection(s2)
print(common_chars('pasta', 'pizza'))

s = 'pasta'
p = 'pizza'


# Returns a dictionary counting charaters in a string
def func2(string):
   d = dict()
   for count in set(string):
      print(set(string))
      d[count] = string.count(count)
      print(d[count])
   return d

print(func2(p))


# Returns a dictionary counting charaters in a string
lambda2 = lambda string: dict([(count, string.count(count)) for count in set(string)])
#print(lambda2(p))

string = 'DataCamp'
v = string[::-1]
print(v)
