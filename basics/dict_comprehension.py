keys = ["age", "name", "height"]
values = [32, "Corina", 1.4]

# Old method

d1 = dict()
for i in range(len(keys)):
    d1[keys[i]] = values[i]
print(d1)

# even more pythonic way
d3 = { key: value for key, value in zip(keys, values) }
print(d3)

# # used destructuring, see below
# # goal is to flatten
# b = [[1, 2], [3, 4], [5, 6]]
# ans = []
# for first, second in b:
#     ans.append(first)
#     ans.append(second)
# print(ans)