def mean_arithmetic(list):
    sum = 0
    for mean in list:
        sum += mean
    mean = round(sum / len(list), 1)
    return mean
def range_of_list(list):
    range = max(list) - min(list) 
    return range
my_list = [1,2,4,6,7]
print(mean_arithmetic(my_list))
print(range_of_list(my_list))