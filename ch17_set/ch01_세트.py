# 세트(set)
# 특징 1. 중복을 허용하지 않는다.
# 특징 2. 순서가 없다.
h = {1, 2 ,3, 4, 5}
hh = set([3,4,5,6,7])

a = set("파이썬은 즐거워")
b = set(["파이썬은 즐거워", "안녕"])
print(a)
print(b)

# c = {1,2,'a','b',(1,2,3)}
# print(c)

# print('hh 길이는',len(hh))
# print(h & hh) # h.intersection(hh)
# print(h | hh) # h.union(hh)
# print(h - hh) # h.difference(hh)

# h.add('안녕')
# print(h)

# h.remove('안녕')
# print(h)

# h.update(['반가워','안녕'])
# print(h)
# h.update('파이썬')
# print(h)

# if 4 in h:
#     print("있다")
# else:
#     print("없다")

# for i in h:
#     print(i)

# 정수, 실수, 복소수, 문자열, 리스트[], 튜플(), 딕셔너리{'1':'일'}, 세트, 불