a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
a1 = set(a)
a2 = list(a1)
print(a2)

# b = {1, 2, 3, 4, 5}
# b1 = set()
# for i in b:
#     b1.add(i*2)
# print(b1)

# b2 = {i*2 for i in b} # 컴프리헨션
# print(b2)

# c = {'a', 'b', 'c', 'd', 'e'}
# for i in enumerate(c):
#     print(i)

# d = {1, 2, 3, 4, 5}
# d1 = {3, 4, 5, 6, 7}
# for i in d & d1:
#     d.remove(i)
#     d1.remove(i)
# print(d)
# print(d1)