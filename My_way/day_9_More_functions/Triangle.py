def triangle(size):
    if size > 0:
        row = 1
        while row <= size:
            print("#" * row)
            row += 1    
    else:
        print("times cannot be negative or zero")
def shape (t_size, t_str, height_sqr, str_sqr):
    row = 1
    while row <= t_size:
        print(t_str[0] * row)    
        row += 1
    square_row = 0
    while square_row < height_sqr:
        print(str_sqr * t_size)
        square_row += 1
shape(5, "a", 5, "g")