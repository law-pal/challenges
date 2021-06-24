from collections import Counter



solution3 = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

crypt3 = ["SEND", "MORE", "MONEY"]
def is_crypt_solution(crypto, solutions):
   solution_to_dict = dict()
   crypt_one = crypt[0]
   crypt_two = crypt[1]
   crypt_three = crypt[2]
   has_zeros = False

   # k = {key, int(value) for key, value in solution}
   # print(k)

   for key, value in solution:
      # converts the list to a dictionary, the key remains a string and the value is converted to an int
      solution_to_dict[key] = int(value)
      # print(solution_to_dict)
   
# if solution_to_dict[crypt_one[0]] == 0 or solution_to_dict[crypt_two[0]] == 0 or solution_to_dict[crypt_three[0]] == 0:
#    print(solution_to_dict[crypt_one[0]])
#    has_zeros = True

   crypt_digits_one = ''.join([str(solution_to_dict[i]) for i in crypt_one])
   crypt_digits_two = ''.join([str(solution_to_dict[i]) for i in crypt_two])
   crypt_digits_three = ''.join([str(solution_to_dict[i]) for i in crypt_three])

   if int(crypt_digits_one) + int(crypt_digits_two) == int(crypt_digits_three):
      return True
   elif int(crypt_digits_one[0]) == 0 and int(crypt_digits_two[0]) == 0:
      return False
   elif int(crypt_digits_one) + int(crypt_digits_two) != int(crypt_digits_three):
      return False
   return True


crypt = ["TEN", "TWO", "ONE"]

solution = [["O","1"], ["T","0"], ["W","9"], ["E","5"], ["N","4"]] # false
#solution2 = [["O","0"], ["T","1"], ["W","2"], ["E","5"], ["N","6"]] # true

crypt2 = ["AA", "AA", "AA"] # false
solution2 = [["A","0"]]
print(is_crypt_solution(crypt, solution))
print(is_crypt_solution(crypt2, solution2))
print(is_crypt_solution(crypt3, solution3))


