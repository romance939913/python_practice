# # list comprehension

# # general list comprehension
# lst = [1, "2", "three", True, None]

# # method 1
# list_1 = []
# for item in lst:
#     list_1.append(item)
# print(list_1)

# # list comprehension method
# lst_2 = [item for item in lst]
# print(lst_2)


# # list comprehension for mapping
# lst = ["jerry", "MARY", "carrIE", "larry"]

# # Old method
# lst_1 = []
# for name in lst:
#     lst_1.append(name.title())
# print(lst_1)

# comprehension method
# lst_2 = [item.title() for item in lst]
# print(lst_2)


# # list comprehension for filtering
# lst = [1, 11, 12, 17, 19, 21, 27, 33, 40]

# # old method
# lst_1 = []
# for num in lst:
#     if num % 3 == 0: 
#         lst_1.append(num)
# print(lst_1)

# # comprehension method
# lst_2 = [num for num in lst if num % 3 == 0]
# print(lst_2)


# nested loop comprehension
# recipe: [item, outer-for-loop inner-for-loop condition]

letters = ["a", "b", "c"]
nums = [1, 2, 3]
# return [(1, "a"), (1, "b"), (1, "c"), (2, "a"), ... ]

# old method
lst_1 = []
for num in nums:
    for char in letters:
        lst_1.append((num, char))
print(lst_1)

# list comprehension method
lst_2 = [(num, letter)
            for num in nums
            for letter in letters]
print(lst_2)
