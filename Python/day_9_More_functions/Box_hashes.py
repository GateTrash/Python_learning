def hash_box (height):
    if height > 0:
        row = 0 
        while row < height:
            print("#" * 10)
            row +=1
    else:
        print("height cannot be negative or zero")
hash_box(9)