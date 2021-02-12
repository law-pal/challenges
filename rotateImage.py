

def rotate_image(matrix):
   """
      Function that rotates a list 90 degrees by transposing a matrix.   
   """
   transpose = [list(i) for i in zip(*matrix)]
   for i in range(len(transpose)):
      for j in range(len(transpose) // 2):
         temp = transpose[i][j]
         transpose[i][j] = transpose[i][len(transpose) - 1 - j]
         transpose[i][len(transpose) - 1 - j] = temp
   return transpose


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    

      
