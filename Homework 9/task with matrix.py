def sum_matrix(matrix, column):
    sum = 0
    for num in matrix:
        sum += num[column -1]
    return sum

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
column = 2
print(sum_matrix(matrix, column))