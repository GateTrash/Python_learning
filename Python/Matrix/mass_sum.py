matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for row in matrix:
    sum = 0
    print(row)
    for element in row:
        sum += element
    print(sum)