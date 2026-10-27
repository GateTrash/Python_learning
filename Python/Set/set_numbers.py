# numbers = [1, 3, 5, 3, 7, 1, 9, 5]
# set_numbers = set(numbers)
# print(f"Count of unique numbers:", len(set_numbers))
# set_numbers.add(11)
# set_numbers.discard(3)
# print(set_numbers)
#_________________________________
# grades = (5, 4, 3, 5, 2, 4, 5)
# print(f"first element: {grades[0]}; last element: {grades[-1]}")
# print(f"Count 5 equal: {grades.count(5)}")
# if 3 in grades:
#     print(f"3 countains in index: {grades.index(3)}")
# else:
#     print("not found")
# if 2 in grades:
#     print("Bad student, you have bad grade!")
# else:
#     print("not found, great job!")
# print(f"count of grades: {len(grades)}")
#________________________________________
# words_str = input("Please, enter words: ").lower()
# words_list = words_str.split()
# words_set = set(words_list)
# print(words_set, f"count unique: {len(words_set)}")
# for word in words_set: print(word)
# print(sorted(words_set))
# 1. Все уникальные слова из обеих групп. +
# 2. Слова, которые встречаются в обеих группах. +
# 3. Слова, которые есть только в первой группе.
# 4. Слова, которые есть только в одной из двух групп.
words_1 = input("Enter first group of words: ").lower().split()
words_2 = input("Enter second group of words: ").lower().split()
set_words1 = set(words_1)
set_words2 = set(words_2)
print(f"unique words from both groups : {set_words1 | set_words2}")
print(f"identical words from both groups : {set_words1 & set_words2}")
print(f"words that are only in the first list : {set_words1 - set_words2}")
print(f"words that are only in the one list : {set_words1 ^ set_words2}")
print(f"words that are only in the second list : {set_words2 - set_words1}")