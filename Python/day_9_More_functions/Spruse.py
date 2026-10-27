def spruse (size):
   if size <= 0:
       print("Size must be greater than 0")
   else:
        print("a spruse!")
        row = 0
        filling_empty = size - 1
        elements = 1
        while row < size:
            print(" " * filling_empty, end= "")
            print("*" * elements)
            filling_empty -= 1
            elements += 2
            row += 1
        print(" " * (size - 1),end= "")
        print("*")
spruse(15)