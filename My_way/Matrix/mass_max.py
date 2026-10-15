matrix = [[12, 5, 8], [3, 25, 7],[9, 4, 16]]
element_max = matrix[0][0]
for row in matrix:
    for element in row:
        if element_max < element:
            element_max = element
print(element_max)