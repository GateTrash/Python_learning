list_1 = [1,3,7,7,9]
list_2 = [5,6,2,3,0]
set_1 = set(list_1)
set_2 = set(list_2)
print("Unique elements:", set_1|set_2)
print("identical elements:", set_1&set_2)
print("Unique elements 1 list:", set_1-set_2)